class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0
        for i, step in enumerate(nums):
            if i<=max_step and (i+step)>max_step:
                max_step = i + step
        return max_step>=len(nums)-1