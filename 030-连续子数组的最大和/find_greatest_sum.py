def find_greatest_sum(array):
    if not array:
        return
    dp = array[0]
    max_sum = array[0]
    for i in range(1, len(array)):
        dp = max(dp, 0) + array[i]
        max_sum = max(max_sum, dp)
    return max_sum
