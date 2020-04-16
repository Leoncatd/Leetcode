class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(cur, l_num, r_num):
            if l_num == 0 and r_num == 0:
                res.append(cur)
                return
            if r_num > 0 and r_num > l_num:
                dfs(cur + ')', l_num, r_num - 1)
            if l_num > 0:
                dfs(cur + '(', l_num - 1, r_num)
        res = []
        dfs('', n, n)
        return res
一般回溯的问题有三种：

Find a path to success 有没有解
Find all paths to success 求所有解
                        求所有解的个数
                        求所有解的具体信息
Find the best path to success 求最优解

回溯法的代码套路是使用两个变量： res 和 path，res 表示最终的结果，path 保存已经走过的路径。如果搜到一个状态满足题目要求，就把 path 放到 res 中。
