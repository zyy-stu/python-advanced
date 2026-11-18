"""使用数据描述符集中校验数值。"""

from __future__ import annotations

from typing import overload


class Positive:
    """将正整数字段保存为实例的独立属性。"""

    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    @overload
    def __get__(self, instance: None, owner: type) -> Positive: ...

    @overload
    def __get__(self, instance: object, owner: type) -> int: ...

    def __get__(self, instance: object | None, owner: type) -> Positive | int:
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance: object, value: int) -> None:
        if type(value) is not int or value <= 0:
            raise ValueError("需要正整数")
        setattr(instance, self.storage_name, value)


class Order:
    """包含至少一件商品的订单。"""

    quantity = Positive()

    def __init__(self, quantity: int) -> None:
        self.quantity = quantity


if __name__ == "__main__":
    print(Order(3).quantity)
