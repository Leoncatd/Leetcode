class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] < target:
                i += 1
            else:
                break
        return i