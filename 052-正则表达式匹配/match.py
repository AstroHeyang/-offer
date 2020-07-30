def match(self, s, pattern):
# write code here
	if not s and not pattern:
	    return True
	if s and not pattern:
	    return False
	if len(pattern) >= 2 and pattern[1] == '*':
	    if s and (pattern[0] == s[0] or pattern[0] == '.'):
	        return (self.match(s,pattern[2:]) or self.match(
	                s[1:],pattern[2:]) or self.match(s[1:],
	                pattern))
	    else:
	        return self.match(s,pattern[2:])
	if s and (s[0] == pattern[0] or pattern[0] == '.'):
	    return self.match(s[1:],pattern[1:])
	return False
