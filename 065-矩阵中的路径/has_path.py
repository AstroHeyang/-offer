class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or not path:
            return False
        
        def isValid(row, col, visited, index):
            if (
                row >= 0 and row < rows and 
                col >= 0 and col < cols and
                not visited[row*cols+col] and 
                path[index] == matrix[row*cols + col]):
                return True
            else:
                return False
            
        def hasPathCore(row, col, visited, index):
            if index == len(path)-1 and isValid(row, col, visited, index):
                return True
            if index < 0:
                return False
            res = False
            if isValid(row, col, visited, index):
                visited[row*cols+col] = True
                index += 1
                res =   hasPathCore(row+1, col, visited, index) or \
                        hasPathCore(row-1, col, visited, index) or \
                        hasPathCore(row, col+1, visited, index) or \
                        hasPathCore(row, col-1, visited, index) 
                if not res:
                    index -= 1
                    visited[row*cols + col] = False
            return res
        
        visited = [False]*rows*cols
        index = 0
        for i in range(rows):
            for j in range(cols):
                if hasPathCore(i, j, visited, index):
                    return True
        return False
