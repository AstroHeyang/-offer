import heapq
class Solution:
    def __init__(self):
        self.heap_max = []
        self.heap_min = []
    
    def adjust(self):
        difference = len(self.heap_min) - len(self.heap_max)
        if difference == 2:
            heapq.heappush(self.heap_max, -heapq.heappop(self.heap_min))
        if difference == -1:
            heapq.heappush(self.heap_min, -heapq.heappop(self.heap_max))
            
    def Insert(self, num):
        # write code here
        if not self.heap_min:
            heapq.heappush(self.heap_min, num)
        elif not self.heap_max:
            heapq.heappush(self.heap_min, num)
            self.adjust()
        else:
            if num >= -self.heap_max[0]:
                heapq.heappush(self.heap_min, num)
            else:
                heapq.heappush(self.heap_max, -num)
            self.adjust()
            
    def GetMedian(self, s):
        # write code here
        if not self.heap_max and not self.heap_min:
            return None
        if (len(self.heap_max) + len(self.heap_min)) % 2 == 1:
            return self.heap_min[0]
        else:
            return (self.heap_min[0] - self.heap_max[0]) / 2.0
