class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        i = 0
        j = n-1
        while(i<j):
            if nums[i]+nums[j]==target:
                return[i+1, j+1]
            elif nums[i]+nums[j]>target:
                j=j-1
            else:
                i =i+1
        return False
