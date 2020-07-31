class Solution:
    # 返回对应char
    def __init__(self):
        self.string = [] 
        self.hashmap = {}
        
    def FirstAppearingOnce(self):
        # write code here
        if not self.string:
            return '#'
        for x in self.string:
            if self.hashmap[x] == 1:
                return x
        return '#'
    
    def Insert(self, char):
        # write code here
        self.string.append(char)
        if char not in self.hashmap:
            self.hashmap[char] = 1
        else:
            self.hashmap[char] += 1
