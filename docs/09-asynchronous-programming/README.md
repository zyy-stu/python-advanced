# 异步编程

本章研究协作式调度与取消。完成后应能解释相关执行过程，并实现具有超时和并发上限的异步任务组。

## 前置知识

[迭代器与生成器](../03-iterators-generators/README.md)、[上下文管理器](../04-context-managers/README.md)

## 课程顺序

1. async 与 await，计划文件 `01-async-await.md`。
2. 协程，计划文件 `02-coroutine.md`。
3. 事件循环，计划文件 `03-event-loop.md`。
4. Task，计划文件 `04-task.md`。
5. gather 与 wait，计划文件 `05-gather-and-wait.md`。
6. 异步 I/O，计划文件 `06-asyncio-io.md`。
7. 异步上下文管理器，计划文件 `07-async-context-manager.md`。
8. 异步生成器，计划文件 `08-async-generator.md`。

## 难点与实践

重点是解释协作式调度与取消的边界，记录实际输出以及失败场景。实践任务：实现具有超时和并发上限的异步任务组。完成后提交一次可复现的验证记录。

上面的文件是后续正式教程的计划路径。章节导读已发布。

[返回教程总目录](../README.md)
