import asyncio
import uuid


async def main():
    # gh-90908 introduces Task Groups for Python 3.11
    # All tasks created within the group tg will complete or error
    # when the with block is done.
    async with asyncio.TaskGroup() as tg:
        tg.create_task(save_log_message("This is an async msg"))
        conf_task = tg.create_task(get_confirmation())

        print("Waiting for tasks to complete...", flush=True)

    print("All tasks have completed now.")

    conf: str = conf_task.result()  # task is done so we have its result.
    print(f"Confirmation is {conf}")


async def save_log_message(text: str):
    await asyncio.sleep(1.5)
    print(f"Saved log message: {text}")
    await asyncio.sleep(.5)


async def get_confirmation() -> str:
    await asyncio.sleep(.5)
    conf = str(uuid.uuid4())
    print("Confirmation ready.")
    return conf


if __name__ == '__main__':
    asyncio.run(main())
