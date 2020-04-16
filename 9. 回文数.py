class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        lst = list(str(x))
        while len(lst)>1:
            if lst.pop(0) != lst.pop():
                return False
        return True
