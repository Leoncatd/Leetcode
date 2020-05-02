class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        left, right = 0, length-1
        curr_max = (length - 1) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                left += 1
                curr_max = max(curr_max, (right-left)*min(height[left], height[right]))
            else:
                right -= 1
                curr_max = max(curr_max, (right-left)*min(height[left], height[right]))
        return curr_max
