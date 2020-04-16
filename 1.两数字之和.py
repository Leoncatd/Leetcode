class Solution(object):
    def twoSum(self, nums, target):
        for idex, num in enumerate(nums):
            for count in range(idex+1, len(nums)):
                if num+nums[count] == target:
                    return [idex, count]
