class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        res = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
        q = collections.deque()
        sum1 = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum1 += grid[i][j]
                if grid[i][j] == 1:
                    res[i][j] = 0
                    q.append([i,j])
        if sum1 == 0 or sum1 == len(grid)* len(grid):
            return -1
        while q:
            x,y = q.popleft()
            for x_index, y_index in [[0,1], [1,0], [0,-1], [-1,0]]:
                new_x = x + x_index
                new_y = y + y_index
                if 0<= new_x <len(grid) and 0<=new_y <len(grid) and res[new_x][new_y] == None:
                    res[new_x][new_y] = res[x][y] + 1
                    q.append([new_x, new_y])
        curr = []
        for a in range(len(res)):
            max1 = max(res[a])
            curr.append(max1)
        max2 = max(curr)

        return max2
