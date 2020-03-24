def get_k_least_numbers(numbers, k):
    if not numbers or len(numbers) < k:
        return None

    def quick_sort(numbers, start, end):
        if start >= end:
            return
        pivot = numbers[start]
        left, right = start, end
        while left < right:
            while left < right and numbers[right] >= pivot:
                right -= 1
            while left < right and numbers[left] <= pivot:
                left += 1
            numbers[left], numbers[right] = numbers[right], numbers[left]
        numbers[start] = numbers[left]
        numbers[left] = pivot
        quick_sort(numbers, start, left-1)
        quick_sort(numbers, left+1, end)
    quick_sort(numbers, 0, len(numbers)-1)
    return numbers[:k]

import heapq
def get_k_least_numbers(numbers, k):
    if not numbers or len(numbers) < k:
        return []
    heapq.heapify(numbers)
    return heapq.nsmallest(k, numbers)
