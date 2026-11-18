# Python 高级知识树

## 01 Python 数据模型

**分类与难点** 学习对象身份与协议，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能用值对象验证相等性和哈希契约。

**前置知识** [Python 基础教程](https://github.com/zyy-stu/python-basic)。

**知识点与推荐顺序** 对象模型 → 对象身份 → 哈希与相等性 → 属性访问 → 特殊方法。

**对应教程路径** [Python 数据模型](../docs/01-python-data-model/README.md)。

## 02 函数高级特性

**分类与难点** 学习函数对象、绑定与调用，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能用闭包实现可配置装饰器并保留签名。

**前置知识** [Python 基础教程](https://github.com/zyy-stu/python-basic)。

**知识点与推荐顺序** 一等函数 → 闭包 → 装饰器 → 高级装饰器 → 函数签名 → 参数传递 → LRU 缓存。

**对应教程路径** [函数高级特性](../docs/02-functions-advanced/README.md)。

## 03 迭代器与生成器

**分类与难点** 学习惰性求值与耗尽，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能把批量读取改为流式处理。

**前置知识** [Python 数据模型](../docs/01-python-data-model/README.md)。

**知识点与推荐顺序** 可迭代对象 → 迭代器 → 生成器 → 生成器表达式 → 委托迭代 → 生成器协程。

**对应教程路径** [迭代器与生成器](../docs/03-iterators-generators/README.md)。

## 04 上下文管理器

**分类与难点** 学习进入退出协议与异常传播，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能用上下文管理器回滚失败操作。

**前置知识** [迭代器与生成器](../docs/03-iterators-generators/README.md)。

**知识点与推荐顺序** with 语句 → 上下文管理协议 → contextlib → 自定义上下文管理器。

**对应教程路径** [上下文管理器](../docs/04-context-managers/README.md)。

## 05 面向对象高级机制

**分类与难点** 学习方法解析与属性绑定，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能建立可复用的字段校验器。

**前置知识** [Python 数据模型](../docs/01-python-data-model/README.md)。

**知识点与推荐顺序** 继承 → 多重继承 → 方法解析顺序 → 协作式 super → property → 描述符 → slots。

**对应教程路径** [面向对象高级机制](../docs/05-object-oriented-advanced/README.md)。

## 06 元编程

**分类与难点** 学习类创建与自省，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能在类创建时验证插件契约。

**前置知识** [面向对象高级机制](../docs/05-object-oriented-advanced/README.md)。

**知识点与推荐顺序** 动态属性 → 动态类 → type 与元类 → 元类 → 类装饰器 → 自省。

**对应教程路径** [元编程](../docs/06-metaprogramming/README.md)。

## 07 内存管理

**分类与难点** 学习对象生命周期与内存观测，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能借助弱引用和快照定位对象滞留。

**前置知识** [Python 数据模型](../docs/01-python-data-model/README.md)。

**知识点与推荐顺序** 引用计数 → 垃圾回收 → 循环引用 → 弱引用 → 内存分析 → 内存优化。

**对应教程路径** [内存管理](../docs/07-memory-management/README.md)。

## 08 并发编程

**分类与难点** 学习共享状态、进程隔离与调度，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能用同一任务对比线程池与进程池。

**前置知识** [Python 数据模型](../docs/01-python-data-model/README.md)。

**知识点与推荐顺序** 多线程 → 线程池 → 多进程 → 进程池 → 队列与锁 → GIL → 并发模型。

**对应教程路径** [并发编程](../docs/08-concurrency/README.md)。

## 09 异步编程

**分类与难点** 学习协作式调度与取消，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能实现具有超时和并发上限的异步任务组。

**前置知识** [迭代器与生成器](../docs/03-iterators-generators/README.md)、[上下文管理器](../docs/04-context-managers/README.md)。

**知识点与推荐顺序** async 与 await → 协程 → 事件循环 → Task → gather 与 wait → 异步 I/O → 异步上下文管理器 → 异步生成器。

**对应教程路径** [异步编程](../docs/09-asynchronous-programming/README.md)。

## 10 类型系统

**分类与难点** 学习静态约束、泛型与结构子类型，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能用 Protocol 隔离存储接口。

**前置知识** [函数高级特性](../docs/02-functions-advanced/README.md)。

**知识点与推荐顺序** 类型注解 → 泛型 → 结构化协议 → TypedDict → 类型变量 → 静态检查 → 高级类型。

**对应教程路径** [类型系统](../docs/10-type-system/README.md)。

## 11 性能优化

**分类与难点** 学习从可重复测量到优化复验，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能对热点函数比较缓存前后的耗时和内存。

**前置知识** [内存管理](../docs/07-memory-management/README.md)、[并发编程](../docs/08-concurrency/README.md)。

**知识点与推荐顺序** 性能分析 → cProfile → timeit → 内存剖析 → 算法优化 → 缓存。

**对应教程路径** [性能优化](../docs/11-performance-optimization/README.md)。

## 12 Python 内部机制

**分类与难点** 学习执行、字节码及导入机制，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能从固定版本的 CPython 源码追踪一次导入。

**前置知识** [Python 数据模型](../docs/01-python-data-model/README.md)。

**知识点与推荐顺序** 执行过程 → 字节码 → 编译与动态执行 → 导入系统 → 导入钩子 → CPython 架构 → 源码阅读。

**对应教程路径** [Python 内部机制](../docs/12-python-internals/README.md)。

## 13 工程化实践

**分类与难点** 学习边界设计、诊断和发布，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能构建可测试、可打包、可部署的应用。

**前置知识** [上下文管理器](../docs/04-context-managers/README.md)、[类型系统](../docs/10-type-system/README.md)。

**知识点与推荐顺序** 项目架构 → 日志 → 测试策略 → 异常设计 → 配置管理 → 打包 → 部署。

**对应教程路径** [工程化实践](../docs/13-engineering-practices/README.md)。

## 14 Python 高级实战项目

**分类与难点** 学习跨机制集成及验收，重点识别何时触发协议、状态变化或资源约束。

**目标与应用** 能用测试验证资源释放与可观测性。

**前置知识** [元编程](../docs/06-metaprogramming/README.md)、[异步编程](../docs/09-asynchronous-programming/README.md)、[性能优化](../docs/11-performance-optimization/README.md)、[工程化实践](../docs/13-engineering-practices/README.md)。

**知识点与推荐顺序** 定义接口 → 实现最小闭环 → 注入故障 → 度量与交付。

**对应教程路径** [Python 高级实战项目](../docs/14-python-advanced-projects/README.md)。

参阅[依赖关系](dependencies.md)和[学习地图](learning-map.md)。
