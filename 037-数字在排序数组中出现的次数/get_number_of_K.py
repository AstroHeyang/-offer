def get_number_of_K(data, k):
    if not data:
        return 0
    if data[0] > k or data[-1] < k:
        return 0
        
    def get_number(k):
        left, right = 0, len(data)-1
        while left <= right:
            mid = (left+right)//2
            if data[mid] > k:
                right -=1
            if data[mid] < k:
                left += 1
                
        return left
        
    return get_number(k+0.5) - get_number(k-0.5)
