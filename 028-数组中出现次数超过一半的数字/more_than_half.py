def more_than_half(numbers):
    if not numbers:
        return 0
    hash_map = {}
    for number in numbers:
        if number not in hash_map:
            hash_map[number] = 1
        else:
            hash_map[number] += 1
    for number in hash_map:
        if hash_map[number] > len(numbers)//2:
            return number
    return 0
