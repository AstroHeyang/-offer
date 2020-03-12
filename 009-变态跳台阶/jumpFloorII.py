# 动态规划
def jumpFloorII(n: int) -> int:
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = 2 * dp[i-1]
    return dp[n]


# 数学归纳法 & 递归
def jumpFloorII(n: int) -> int:
    if n == 0:
        return 0
    return 2 ** (n-1)
