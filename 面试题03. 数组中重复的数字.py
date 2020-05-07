class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 0
            else:
                return i

            