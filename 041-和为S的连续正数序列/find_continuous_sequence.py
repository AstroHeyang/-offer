def find_continuous_sequence(tsum):
	left, right = 1, 2
	res = []
	if tsum <= 0:
		return 

    def getSum(small,large):
		return (small+large)*(large-small+1)//2

    while right <= tsum//2+1 and left < right:
		cur_sum = getSum(left, right)
        if cur_sum == tsum:
            res.append(list(range(left, right+1)))
            right += 1
        elif cur_sum < tsum:
            right += 1
        else:
            left += 1
    return res
