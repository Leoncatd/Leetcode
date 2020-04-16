class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        q = collections.deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    q.append([i,j])
        while q:
            x, y = q.popleft()
            for x_index, y_index in [[1,0], [-1,0], [0,1], [0,-1] ]:
                new_x = x + x_index
                new_y = y + y_index
                if 0<= new_x < len(matrix) and 0 <= new_y <len(matrix[0]) and res[new_x][new_y] == None:
                    res[new_x][new_y] =res[x][y] + 1
                    q.append([new_x,new_y])
        return res
