class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length = []
        ls = []
        for i in s:
            if i in ls:
                length.append(len(ls))
                start_idx = ls.index(i) + 1
                ls = ls[start_idx:]
            ls.append(i)
        length.append(len(ls))
        max_length = max(length)
        return max_length
