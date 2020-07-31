def maxInWindows(self, num, size):
   # write code here
   if not num or not size or len(num) < size:
       return []
   window, res = [], []
   for i,x in enumerate(num):
       if i >= size and i-size >= window[0]:
           window.pop(0)
       while window and num[window[-1]] <= x:
           window.pop()
       window.append(i)
       if i >= size-1:
           res.append(num[window[0]])
   return res
