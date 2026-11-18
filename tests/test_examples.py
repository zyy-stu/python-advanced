"""验证独立示例及关键失败路径。"""

import asyncio
import runpy
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1] / "examples"


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("iterators/countdown.py", "[3, 2, 1]"),
        ("decorators/closure.py", "你好，小林 你好，小林"),
        ("context-managers/temporary_value.py", "调试\n普通"),
        ("descriptors/positive.py", "3"),
        ("asyncio/concurrent_tasks.py", "[9, 1, 4]"),
    ],
)
def test_example_output(path: str, expected: str) -> None:
    """以公开命令独立运行脚本。"""
    result = subprocess.run(
        [sys.executable, "-X", "utf8", str(ROOT / path)],
        capture_output=True,
        encoding="utf-8",
        check=True,
        timeout=10,
    )
    assert result.stdout.rstrip("\n") == expected
    assert result.stderr == ""


def test_countdown_exhaustion() -> None:
    """耗尽后重复调用仍抛出 StopIteration。"""
    factory = runpy.run_path(ROOT / "iterators/countdown.py")["Countdown"]
    iterator = factory(0)
    for _ in range(2):
        with pytest.raises(StopIteration):
            next(iterator)


def test_descriptor_rejects_non_positive_value() -> None:
    """描述符拒绝无效赋值。"""
    order = runpy.run_path(ROOT / "descriptors/positive.py")["Order"]
    with pytest.raises(ValueError, match="正整数"):
        order(0)


def test_context_restores_on_error() -> None:
    """退出时恢复数据，并将异常传给外层。"""
    manager = runpy.run_path(ROOT / "context-managers/temporary_value.py")["TemporaryValue"]
    options = {"mode": "普通"}
    with pytest.raises(RuntimeError, match="失效"), manager(options, "mode", "调试"):
        assert options["mode"] == "调试"
        raise RuntimeError("失效")
    assert options["mode"] == "普通"


def test_batch_rejects_zero_limit() -> None:
    """禁止无法取得信号量的配置。"""
    run_batch = runpy.run_path(ROOT / "asyncio/concurrent_tasks.py")["run_batch"]
    with pytest.raises(ValueError, match="并发上限"):
        asyncio.run(run_batch([1], 0))
