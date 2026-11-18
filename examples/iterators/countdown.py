"""使用迭代协议逐项生成倒计时。"""

from collections.abc import Iterator
from typing import Self


class Countdown(Iterator[int]):
    """步进到零后保持耗尽。"""

    def __init__(self, start: int) -> None:
        self.remaining = start

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.remaining <= 0:
            raise StopIteration
        value = self.remaining
        self.remaining -= 1
        return value


if __name__ == "__main__":
    print(list(Countdown(3)))
