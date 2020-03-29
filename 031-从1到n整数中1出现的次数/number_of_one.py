def getNumberOf1(n):
    if n == 0:
        return 0
    if n < 10:
        return 1
    first = int(str(n)[0])
    last = int(str(n)[1:])
    digits = len(str(n)) - 1
    if first == 1:
        return (int(last) + 1 + getNumberOf1(last)
                + getNumberOf1Digits(digits))
    elif first > 1:
        return (10 ** digits + getNumberOf1(last)
                + first * getNumberOf1Digits(digits))


# 获取1-9 (digit=1), 1-99 (digit=2)，...的1的个数
def getNumberOf1Digits(digits):
    return digits * 10 ** (digits - 1)


