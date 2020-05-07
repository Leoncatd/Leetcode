class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False
        x = 0
        y = cols - 1
        while x < rows and y >= 0:
            if target < matrix[x][y]:
                y -= 1
            elif target > matrix[x][y]:
                x += 1
            elif target == matrix[x][y]:
                return True

        return False