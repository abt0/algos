# O(n^2)


def arithmetic_series(n: int) -> int:
    if n < 0:
        raise ValueError('Argument n is not a natural number')

    return int((n + 1) * n * 0.5)


def arithmetic_series_loop(n: int) -> int:
    if n < 0:
        raise ValueError('Argument n is not a natural number')

    s: int = 0

    while n > 0:
        s += n
        n -= 1

    return s
