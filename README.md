# Python 高级教程

## 定位与目标

Python Learning Roadmap 的中文高级教程仓库。面向已掌握基础语法、函数、类、模块和异常的开发者，学习语言协议、运行时、调度与工程化，并用示例、测试与源码验证结论。入门内容见 [Python 基础教程](https://github.com/zyy-stu/python-basic)。

## 高级知识体系与导航

[完整知识树](knowledge-tree/README.md)覆盖 Python 数据模型、函数高级特性、迭代器与生成器、上下文管理器、面向对象高级机制、元编程、内存管理、并发编程、异步编程、类型系统、性能优化、Python 内部机制、工程化实践、Python 高级实战项目。[教程总目录](docs/README.md)列出 14 章与每篇规划文件。[开发路线图](ROADMAP.md)记录待开发任务。

## 学习路线

[中级路线](learning-path/intermediate.md)从协议、函数和对象模型切入。[专家路线](learning-path/expert.md)延伸到实现、内存、并发和性能。按[知识依赖](knowledge-tree/dependencies.md)和[学习地图](knowledge-tree/learning-map.md)选择顺序。

## 示例与项目

从[五个可运行示例](examples/README.md)入手。综合项目见[缓存框架、任务调度器、异步采集器与插件系统](projects/README.md)。

## 开发环境

使用 Python 3.11+。示例仅依赖标准库。运行检查前建议创建虚拟环境并安装开发依赖。

```bash
python -m pip install -r requirements-dev.txt
python -m ruff check .
python -m ruff format --check .
python -m pytest
```

## 贡献、规范与许可证

使用[贡献指南](CONTRIBUTING.md)、[教程规范](standards/README.md)和[编写模板](templates/README.md)。项目采用 [MIT 许可证](LICENSE)。

## 其他专题仓库

- [python-learning-roadmap](https://github.com/zyy-stu/python-learning-roadmap)
- [python-basic](https://github.com/zyy-stu/python-basic)
- [python-web](https://github.com/zyy-stu/python-web)
- [python-data-science](https://github.com/zyy-stu/python-data-science)
- [python-ai](https://github.com/zyy-stu/python-ai)
- [python-projects](https://github.com/zyy-stu/python-projects)
