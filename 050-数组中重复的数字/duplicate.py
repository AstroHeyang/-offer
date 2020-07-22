def duplicate(numbers, duplication):
	if not numbers:
	    return False 
	for num in numbers:
	    if num < 0 or num > len(numbers)-1:
	        return False
	for i, num in enumerate(numbers):
	    while i != numbers[i]:
	        num = numbers[i]
	        if numbers[i] == numbers[num]:
	            duplication[0] = num
	            return True
	        numbers[i], numbers[num] = numbers[num], numbers[i]
	return False
