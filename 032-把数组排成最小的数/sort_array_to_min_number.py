from functools import cmp_to_key


def PrintMinNumber(numbers):
    if not numbers:
        return ''
    numbers = list(map(str, numbers))
    cmp2keys = cmp_to_key(lambda x, y: int(x+y) - int(y+x))
    numbers.sort(key=cmp2keys)
    return ''.join(numbers)