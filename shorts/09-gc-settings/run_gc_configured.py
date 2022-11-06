import datetime
import gc
import os
import random

import psutil
from colorama import Fore


def main(change_gc: bool):
    count = 1000
    times = 100

    # gc.set_debug(True)
    gc.freeze()

    m0 = report_process_mem()

    if change_gc:
        # g0, g1, allocs = gc.get_threshold()
        # gc.set_threshold(g0 * 5, g1 * 10, 100_000)

        allocs, gen1, gen2 = gc.get_threshold()
        allocs = 50_000  # Start the GC sequence every 10K not 700 class allocations.
        gc.set_threshold(allocs, gen1 * 5, gen2 * 10)

    lists_of_items = []
    for items in range(0, times):
        lists_of_items.append(create_some_items(count))

    m1 = report_process_mem()

    return change_gc, m1 - m0


def report_process_mem() -> int:
    process = psutil.Process(os.getpid())
    mb = process.memory_info().rss / 1024 / 1024
    print(f"Total memory used: {mb:,.2f} MB.")

    return mb


class DbItem:
    def __init__(self, x: float, y: list[dict]):
        self.x = x
        self.y = y


def create_some_items(count: int) -> list[DbItem]:
    items = []

    for _ in range(0, count):
        lst = [{} for _ in range(0, 20)]
        item = DbItem(random.random(), lst)
        items.append(item)

    return items


if __name__ == '__main__':
    random.seed(12345)
    create_some_items(1)

    change_gc = input("Use modified GC settings? [y]/n ") in {'', 'y'}

    t0 = datetime.datetime.now()
    changed_gc, mem_delta = main(change_gc)

    dt = datetime.datetime.now() - t0
    msg = (Fore.LIGHTRED_EX + 'with') if changed_gc else (Fore.CYAN + 'without')
    print(f"Done {msg + Fore.RESET} modifying the GC.")
    print(f'Memory used: {mem_delta:,.0f} MB')
    print(f'Time:{Fore.LIGHTYELLOW_EX} {dt.total_seconds() * 1000:,.1f} ms')
