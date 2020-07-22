def reverse_sentence(s):
	if not s:
        return ''
    if len(s) <= 1:
        return s 
    return ' '.join(s.split(' ')[::-1])
