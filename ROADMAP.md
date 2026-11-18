# 高级教程开发路线图

任务状态均为待开发。章节索引登记全部计划文件；下表列出优先建设的 20 项。交付时应用[教程标准](standards/tutorial-standard.md)。

| 编号 | 主题 | 前置知识 | 预期成果 | 对应文件 | 验收 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| PA-001 | 对象模型 | Python 基础 | 机制讲解、可运行示例和练习 | `docs/01-python-data-model/01-object-model.md` | 验证类型、身份和相等性 | 待开发 |
| PA-002 | 特殊方法 | 属性访问 | 机制讲解、可运行示例和练习 | `docs/01-python-data-model/05-special-methods.md` | 展示运算分派与回退 | 待开发 |
| PA-003 | 闭包 | 一等函数 | 机制讲解、可运行示例和练习 | `docs/02-functions-advanced/02-closures.md` | 验证闭包捕获和状态 | 待开发 |
| PA-004 | 装饰器 | 闭包 | 机制讲解、可运行示例和练习 | `docs/02-functions-advanced/03-decorators.md` | 验证签名保留及异常传播 | 待开发 |
| PA-005 | 迭代器 | 可迭代对象 | 机制讲解、可运行示例和练习 | `docs/03-iterators-generators/02-iterator.md` | 验证耗尽和重复迭代 | 待开发 |
| PA-006 | 生成器 | 迭代器 | 机制讲解、可运行示例和练习 | `docs/03-iterators-generators/03-generator.md` | 验证惰性、关闭和清理 | 待开发 |
| PA-007 | 上下文管理协议 | with 语句 | 机制讲解、可运行示例和练习 | `docs/04-context-managers/02-context-manager-protocol.md` | 验证正常退出和异常传播 | 待开发 |
| PA-008 | 方法解析顺序 | 多重继承 | 机制讲解、可运行示例和练习 | `docs/05-object-oriented-advanced/03-mro.md` | 输出菱形继承的 MRO | 待开发 |
| PA-009 | 描述符 | property | 机制讲解、可运行示例和练习 | `docs/05-object-oriented-advanced/06-descriptors.md` | 验证类与实例访问顺序 | 待开发 |
| PA-010 | 元类 | type 与元类 | 机制讲解、可运行示例和练习 | `docs/06-metaprogramming/04-metaclass.md` | 验证类创建与注册顺序 | 待开发 |
| PA-011 | 引用计数 | Python 数据模型 | 机制讲解、可运行示例和练习 | `docs/07-memory-management/01-reference-counting.md` | 区分语言语义和 CPython 引用计数 | 待开发 |
| PA-012 | 垃圾回收 | 引用计数 | 机制讲解、可运行示例和练习 | `docs/07-memory-management/02-garbage-collection.md` | 重现循环对象的回收 | 待开发 |
| PA-013 | 多线程 | Python 数据模型 | 机制讲解、可运行示例和练习 | `docs/08-concurrency/01-threading.md` | 在可重复测试中验证同步边界 | 待开发 |
| PA-014 | 多进程 | 线程池 | 机制讲解、可运行示例和练习 | `docs/08-concurrency/03-multiprocessing.md` | 验证启动入口和跨进程序列化 | 待开发 |
| PA-015 | GIL | 队列与锁 | 机制讲解、可运行示例和练习 | `docs/08-concurrency/06-gil.md` | 说明版本和构建差异 | 待开发 |
| PA-016 | async 与 await | 迭代器与生成器、上下文管理器 | 机制讲解、可运行示例和练习 | `docs/09-asynchronous-programming/01-async-await.md` | 验证任务顺序、超时与取消 | 待开发 |
| PA-017 | 类型注解 | 函数高级特性 | 机制讲解、可运行示例和练习 | `docs/10-type-system/01-type-hints.md` | 给出静态检查通过和失败的例子 | 待开发 |
| PA-018 | 性能分析 | 内存管理、并发编程 | 机制讲解、可运行示例和练习 | `docs/11-performance-optimization/01-performance-analysis.md` | 给出固定输入和可重复基线 | 待开发 |
| PA-019 | 执行过程 | Python 数据模型 | 机制讲解、可运行示例和练习 | `docs/12-python-internals/01-python-execution.md` | 用 dis 验证执行步骤与版本 | 待开发 |
| PA-020 | 源码阅读 | CPython 架构 | 机制讲解、可运行示例和练习 | `docs/12-python-internals/07-source-code-reading.md` | 用固定标签给出可复现调用链 | 待开发 |
