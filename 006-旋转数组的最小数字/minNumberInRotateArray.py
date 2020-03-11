def minNumberInRotateArray(rotateArray):
    if not rotateArray:
        return 0
    left, right = 0, len(rotateArray)-1
    while left < right:
        mid = [left+right]//2
        if rotateArray[left] == rotateArray[mid] and \
                rotateArray[right] == rotateArray[mid]:
            for i in range(left, right):
                if rotateArray[i] < rotateArray[i+1]:
                    return rotateArray[i]
            return rotateArray[right]
        else:
            if rotateArray[mid] <= rotateArray[right]:
                right = mid
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            if left == right-1:
                return rotateArray[right]
    return rotateArray[left]
