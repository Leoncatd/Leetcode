class Solution:
    def jump(self, nums: List[int]) -> int:
        max_bound = 0
        end = 0
        step = 0
        for i in range(len(nums)-1):
            max_bound = max(max_bound, i+nums[i])
            if i == end:
                end = max_bound
                step += 1
        return step
