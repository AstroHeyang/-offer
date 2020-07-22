def multiply(A):
	if not A:
		return []
	res = 1 * len(A)
	for i in range(1, len(A)):
	    for j in range(i):
	        res[i] *= A[j]
	        
	for i in range(len(A)-2, -1, -1):
	    for j in range(len(A)-1, i, -1):
	        res[i] *= A[j]
	return res

