res = []


def print_matrix(matrix):
    if not matrix:
        return
    start = 0
    while len(matrix) > 2*start and len(matrix[0]) > 2*start:
        print_circle(matrix, len(matrix), len(matrix[0]), start)
        start += 1
    return res


def print_circle(matrix, nRow, nCol, start):
    if not nRow or not nCol:
        return

    endRow = nRow - start -1
    endCol = nRow - start -1
    for i in range(start, endCol+1):
        res.append(matrix[start][i])
    if endRow - start >= 1 and endCol > start:
        for j in range(start+1, endRow+1):
            res.append(matrix[j][endCol])
    if endCol - start >= 2 and endRow > start:
        for i in range(endCol-1, start, -1):
            res.append(matrix[endRow][i])
    if endRow - start >= 1 and endCol > start:
        for j in range(endRow, start, -1):
            res.append(matrix[j][start])
