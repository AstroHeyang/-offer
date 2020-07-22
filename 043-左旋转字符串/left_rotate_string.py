def left_rotate_string(s, n):
	if not s:
		return s
    n = n % len(s)
    return s[n:] + s[:n] 
