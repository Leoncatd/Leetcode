class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        for i in range(1,len(nums)):
            dp.append(max(nums[i], nums[i]+dp[i-1]))
        return max(dp)
