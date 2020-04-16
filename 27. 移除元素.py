class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        flag = 0
        for i in range(length):
            if nums[i] != val:
                nums[flag] = nums[i]
                flag += 1
        return flag
