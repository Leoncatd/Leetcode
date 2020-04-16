class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0 or length < 0:
            return
        index = 0
        for i in range(length):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        for j in range(index, length):
            nums[j] = 0
