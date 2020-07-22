def last_remaining(n, m):
	if not n or not m:
		return -1
    list_n = list(range(n))
    start = 0
	while len(list_n) > 1:
		pop_index = (start+m-1)% len(list_n)
        list_n.pop(pop_index)
        start = 0 if pop_index == len(list_n) else pop_index
    return list_n[0]
