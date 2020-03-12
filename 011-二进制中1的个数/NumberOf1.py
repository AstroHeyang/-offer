def NumberOf1(n: int) -> int:
    if n < 0:
        n = n & 0xffffffff
    count = 0
    while n > 0:
        n = n & (n-1)
        count += 1
    return count

