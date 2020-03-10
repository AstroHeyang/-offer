def find(target: int, array: list) -> bool:
    if not target or not array:
        return False
    row, col = 0, len(array[0])-1
    while row < len(array) and col >= 0:
        if array[row][col] == target:
            return True
        elif array[row][col] > target:
            col -= 1
        else:
            row += 1
    return False

