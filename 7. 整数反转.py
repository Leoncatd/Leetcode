class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        num = len(s)
        result = [0]*num
        if x > (2**32)/2-1 or x < (-2**32)/2:
            return 0
        list1 = list(s)
        if x < 0:
            i = num-1
            j = 0
            while i > 0:
                result[j] = list1[i]
                i-=1
                j+=1
            result = result[:num-1]
            result = ''.join("%s" %id for id in result)
            result = int(result) * -1
        else:
            i = num-1
            j = 0
            while i>=0:
                result[j] = list1[i]
                i-=1
                j+=1
            result = ''.join("%s" %id for id in result)
            result = int(result)
        if result  > (2**32)/2-1 or result < (-2**32)/2:
            return 0
        else:
            return result
