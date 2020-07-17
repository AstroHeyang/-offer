count = 0
def inverse_pairs(data):
    global count
    def merge_sort(lists):
        global count
        if len(lists) <= 1:
            return lists
        num = len(lists) // 2 
        left = merge_sort(lists[:num])
        right = merge_sort(lists[num:])
        l, r = 0, 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
                count += len(left)-l
            result += right[r:]
            result += left[l:]
        return result
    merge_sort(data)
    return count%1000000007
