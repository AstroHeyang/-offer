# 递归
def power(base: float, n: int) -> float:
    if base == 0:
        return None
    if n == 0:
        return 1
    sign = 1
    if n < 0:
        base = 1 / base
        n = -n
    if n % 2 == 0:
        return power(base*base, n >> 1)
    if n % 2 == 1:
        return power(base*base, n >> 1) * base


# 非递归
def power(base: float, n: int) -> float:
    if base == 0:
        return None
    if n == 0:
        return 1
    if n < 0:
        base = 1 / base
        n = -n
    res = 1
    while n > 0:
        if n % 2 == 1:
            res *= base
        n >>= 1
        base *= base
    return res

