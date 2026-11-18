"""离开上下文时恢复映射，异常继续向调用方传播。"""

from types import TracebackType
from typing import Self


class TemporaryValue:
    """在一个上下文中覆盖单个已存在的键。"""

    def __init__(self, data: dict[str, str], key: str, value: str) -> None:
        self.data = data
        self.key = key
        self.value = value

    def __enter__(self) -> Self:
        self.previous = self.data[self.key]
        self.data[self.key] = self.value
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.data[self.key] = self.previous


if __name__ == "__main__":
    options = {"mode": "普通"}
    try:
        with TemporaryValue(options, "mode", "调试"):
            print(options["mode"])
            raise ValueError("模拟错误")
    except ValueError:
        print(options["mode"])
