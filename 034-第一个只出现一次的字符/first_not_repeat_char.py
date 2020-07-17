def FirstNotRepeatingChar(self, s):
        # write code here
        if not s :
            return -1
        strMap = {}
        for i,x in enumerate(s):
            if x not in strMap:
                strMap[x] = [i]
            else:
                strMap[x].append(i)
        res = []
        for j in strMap:
            if len(strMap[j]) == 1:
                res.append(strMap[j][0]) 
        return min(res) if res else -1
