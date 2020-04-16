class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nus = sorted(list(set(nums)))
        for i in range(len(nus)):
            nums[i] = nus[i]
        return len(nus)
