"""用任务组和信号量运行有上限的异步批次。"""

import asyncio


async def run_batch(values: list[int], limit: int) -> list[int]:
    """保持输入顺序返回结果，任务组负责等待或取消。"""
    if limit < 1:
        raise ValueError("并发上限至少为一")
    semaphore = asyncio.Semaphore(limit)

    async def work(value: int) -> int:
        async with semaphore:
            await asyncio.sleep(0.01)
            return value * value

    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(work(value)) for value in values]

    return [task.result() for task in tasks]


if __name__ == "__main__":
    print(asyncio.run(run_batch([3, 1, 2], 2)))
