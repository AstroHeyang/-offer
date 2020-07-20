def find_number_appear_once(array):
	if not array:
        return None
    f = lambda x,y:x^y
    pivot = reduce(f, array)

    def isBit1(num,index):
		while index > 0:
			num >>= 1
			index -= 1
		return (num & 1)

	def getBit1Index(num):
		index = 0
		while not (num & 1):
			num >>= 1
			index += 1
		return index

	index = getBit1Index(pivot)

	arrayPart1, arrayPart2 = [],[]
	for x in array:
		if isBit1(x,index):
			arrayPart1.append(x)
		else:
			arrayPart2.append(x)
	num1 = reduce(f, arrayPart1)
	num2 = reduce(f, arrayPart2)
	return [num1,num2]
