class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}', '[':']', '?':'?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif c != dic[stack.pop()]:
                return False
        return len(stack)==1
Tips:
    当stack是空时，stack.pop()会报错，所以初始stack为？，并且在字典中构造对应关系，这样stack为空或者c为右括号时可以返回False
