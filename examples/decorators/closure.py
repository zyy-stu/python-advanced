"""用闭包传入重复次数，以装饰器组合字符串处理。"""

from collections.abc import Callable
from functools import wraps
from typing import ParamSpec

P = ParamSpec("P")


def repeat(times: int) -> Callable[[Callable[P, str]], Callable[P, str]]:
    """生成保留被装饰函数元数据的包装器。"""
    if times < 1:
        raise ValueError("重复次数至少为一")

    def decorate(function: Callable[P, str]) -> Callable[P, str]:
        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> str:
            return " ".join(function(*args, **kwargs) for _ in range(times))

        return wrapper

    return decorate


@repeat(2)
def greet(name: str) -> str:
    """返回问候语。"""
    return f"你好，{name}"


if __name__ == "__main__":
    print(greet("小林"))
