class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while (right-left)>1:
            if isBadVersion((right+left)//2 ):
                right = (right+left)//2
            else:
                left = (right+left)//2
        if isBadVersion(left):
            return left
        else :
            return right
