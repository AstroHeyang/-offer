def jumpFloor(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    first, second = 1, 2
    while n > 2:
        first, second = second, first + second
        n -= 1
    return second
