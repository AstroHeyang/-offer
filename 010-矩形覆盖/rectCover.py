def rectCover(n: int, first=1, second=2) -> int:
    if n <= 1:
        return first
    if n == 2:
        return second
    return rectCover(n-1, second, first+second)