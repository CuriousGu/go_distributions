from functools import lru_cache


@lru_cache(maxsize=1000)
def factorial(n: int) -> int:
    return n * factorial(n-1) if n else 1


def combinatory(n: int, x: int) -> int:
    return factorial(n) / (factorial(x) * factorial(n-x))
