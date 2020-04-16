class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length1 = len(haystack)
        length2 = len(needle)
        if haystack == '' and needle == '':
            return 0
        index = 0
        while index <= length1 - length2:
            if haystack[index:index+length2] == needle:
                return index
            index += 1
        return -1
