from typing import Union


def hundreds(x: Union[int, float]) -> int:
    return (int(x) // 100) % 10


hundreds(100.0)
hundreds(100)
hundreds("avs")
