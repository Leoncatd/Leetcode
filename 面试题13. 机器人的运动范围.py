class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def add(a, b):
            add_sum = 0
            while a > 0:
                add_sum += a % 10
                a = a // 10
            while b > 0:
                add_sum += b % 10
                b = b // 10
            return add_sum

        lst = [[None for _ in range(n)] for _ in range(m)]
        q = collections.deque()
        result = 0
        lst[0][0] = 1
        q.append([0, 0])

        while q:
            x, y = q.popleft()
            result += 1
            for x_index, y_index in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_x = x + x_index
                new_y = y + y_index
                if new_x < 0 or new_y < 0 or new_x > m - 1 or new_y > n - 1 or lst[new_x][new_y] == 1 or add(new_x,
                                                                                                             new_y) > k:
                    continue
                lst[new_x][new_y] = 1
                q.append([new_x, new_y])

        return result
