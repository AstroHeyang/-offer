def cut_rope(number):
	if number == 2:
	    return 1
	if number == 3:
	    return 2
	if number % 3 == 0:
	    return 3**(number//3)
	if number % 3 == 1:
	    return 3**(number//3-1)*4
	if number % 3 == 2:
	    return 3**(number//3)*2
