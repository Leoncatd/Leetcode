class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in nums:
            if index < 2 or i != nums[index - 2]:
                nums[index] = i
                index += 1
        return index
