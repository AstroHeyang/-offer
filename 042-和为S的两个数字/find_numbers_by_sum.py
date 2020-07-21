def find_numbers_by_sum(array, tsum):
	if not array:
		return []
	left, right = 0, len(array)-1
	while left < right:
		target = array[left] + array[right]
        if target == tsum:
            return [array[left], array[right]]
        elif target < tsum:
            left += 1
        else:
            right -= 1
    return []
