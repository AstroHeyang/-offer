def fibonacci(n: int, first=1, second=1) -> int:
    if n <= 1:
        return first
    if n == 2:
        return second
    return fibonacci(n-1, second, first+second)