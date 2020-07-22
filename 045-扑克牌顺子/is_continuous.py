def is_continuous(numbers):
    if len(numbers) < 5:
        return False
    count_0 = 0
    numbers.sort()
    for i,x in enumerate(numbers):
		if x == 0:
            count_0 += 1
        else:
			if i+1 < len(numbers) and x == numbers[i+1]:
                return False
            if i+1 < len(numbers) and numbers[i+1] - x > 1:
                count_0 -= numbers[i+1] - x -1
                if count_0 < 0:
                    return False
    return True
