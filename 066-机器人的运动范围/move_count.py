class Solution:
    def movingCount(self, threshold, rows, cols):
        visited = []
        if threshold < 0:
            return 0
        
        def out_of_bound(array):
            if array[0] < 0 or array[0] > rows-1 \
                or array[1] < 0 or array[1] > cols-1:
                    return True
                
        def sum_pixel(array):
            sum_current = 0
            row, col = array[0], array[1]
            while row:
                sum_current += row % 10
                row //= 10
            while col:
                sum_current += col % 10
                col //= 10
            return sum_current
        
        def legal_move(array):
            if not out_of_bound(array) and sum_pixel(array) <= threshold \
                and array not in visited:
                return True
            else:
                return False
        
        def moves(x, y):
            count = 0
            if legal_move([x, y]):
                visited.append([x, y])
                count =  1 + moves(x+1, y) + moves(x-1, y) + \
                    moves(x, y+1) + moves(x, y-1)
            return count
        total_count = moves(0,0)
        return total_count
