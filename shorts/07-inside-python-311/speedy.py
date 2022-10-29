# Python 3.11 is 10-60% faster than 3.10
import datetime
import random
import sys
from typing import Tuple


def find_some_distances(points):
    t0 = datetime.datetime.now()

    for (x1, y1), (x2, y2) in points:
        distance = ((x1 - x2) ** 2.0 + (y1 - y2) ** 2.0) ** 0.5


    dt = datetime.datetime.now() - t0
    # print(f"Computed distance for {len(points):,} points in {dt.total_seconds()*1000:,.0f} ms on "
    #       f"Python {sys.version_info.major}:{sys.version_info.minor}")
    return dt.total_seconds()


if __name__ == '__main__':
    warm_up_data = [(1,1),(2,2), (3,3)]
    warmup = list(zip(warm_up_data[:-1], warm_up_data[1:]))
    find_some_distances(warmup)

    larger_data = [
        (random.random(),random.random(),)
        for _ in range(1, 1_000_000+1)
    ]
    larger = list(zip(larger_data[:-1], larger_data[1:]))

    times = []
    for _ in range(1, 100):
        times.append(find_some_distances(larger))

    # ave_sec = sum(times)/len(times)
    ave_sec = min(times)

    print(f"Done in min {ave_sec*1000:,.1f} ms for {sys.version_info.major}:{sys.version_info.minor}")
