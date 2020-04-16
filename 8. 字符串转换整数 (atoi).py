class Solution:
    def myAtoi(self, str: str) -> int:
        flag, ans = None, []
        for i in str:
            if i == " " and not flag and not ans:
                continue
            elif i in "+-" and not flag and not ans:
                flag = (1 if i=="+" else -1)
            elif i in "0123456789":
                ans.append(i)
            else:
                break
        if not ans:
            return 0
        result = int(''.join(ans)) * (flag if flag else 1)
        return result if -2**31<=result<=2**31-1 else ( 2**31-1 if result >0 else -2**31)
