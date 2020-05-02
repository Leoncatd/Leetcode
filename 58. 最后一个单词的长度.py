class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        else:
            words = s.split()
            return len(words[-1]) if words else 0
