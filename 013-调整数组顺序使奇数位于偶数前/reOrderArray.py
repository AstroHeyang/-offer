# 遍历，需要额外空间
def reOrderArray(array: list) -> list:
    if not array:
        return array
    odd, even = [], []
    for i in array:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd + even


# 插入排序思想，不需要额外空间
def reOrderArray(array: list) -> list:
    if not array:
        return array
    k = 0  # 已经排好的奇数个数
    for i in range(len(array)):
        if array[i] % 2 == 1:
            j, tmp = i, array[i]
            while j > k:
                array[j] = array[j - 1]
                j -= 1
            array[k] = tmp
            k += 1
    return array
