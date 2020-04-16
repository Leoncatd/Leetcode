class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.res = ""
        def f(i,j):
            while i >= 0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            if len(self.res) < j-i-1:
                self.res = s[i+1:j]
        for i in range(n):
            f(i,i)
            f(i,i+1)
        return self.res
