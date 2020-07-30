def is_numeric(s):
	# write code here
	# signal表示符号，decimal表示小树点，hasE表示含有符号e
	signal, decimal, hasE = False, False, False
	for i,x in enumerate(s):
	    if x == 'e' or x == 'E':
	        if i == len(s)-1:
	            return False
	        if hasE:
	            return False
	        hasE = True
	    elif x in '+-':
	        if not signal and (i > 0 and s[i-1] not in 'eE'):
	            return False
	        if signal and s[i-1] not in 'eE':
	            return False               
	        signal = True
	    elif x == '.':
	        if decimal:
	            return False
	        if hasE:
	            return False
	        decimal = True
	    elif x not in '0123456789':
	        return False
	return True
