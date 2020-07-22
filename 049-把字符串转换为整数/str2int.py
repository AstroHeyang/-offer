def str2int(s):
	if not s:
        return 0
    sign = '+'
    if s[0] in ['+','-']:
        sign = s[0]
        s = s[1:]
    numStr = [_ for _ in s][::-1]
    numsMap = '0123456789'
    res = 0
	for i,num in enumerate(numStr):
	    if num not in numsMap:
	        return 0
	    res += int(num)*(10**i)
	if sign == '-':
	    res = -res
	if res <= -2147483649 or res >= 2147483648:
	    return 0
	return res
