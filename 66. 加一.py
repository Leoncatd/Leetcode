class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ""
        for i in digits:
            str1 = str1 + str(i)
        int1 = int(str1)
        int1 += 1
        str2 = str(int1)
        res = list(str2)
        for j in range(len(res)):
            res[j] = int(res[j])
        return res
