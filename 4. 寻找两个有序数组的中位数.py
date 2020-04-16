class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        s = m + n - 1
        nums3 = [0] * (m + n)
        m -= 1
        n -= 1
        if m < 0:
            nums3[:n + 1] = nums2[:n + 1]
        if n < 0:
            nums3[:m + 1] = nums1[:m + 1]
        while m >= 0 and n >= 0:
            if nums2[n] > nums1[m]:
                nums3[s] = nums2[n]
                s -= 1
                n -= 1
                if n < 0:
                    nums3[:m + 1] = nums1[:m + 1]
            else:
                nums3[s] = nums1[m]
                s -= 1
                m -= 1
                if m < 0:
                    nums3[:n + 1] = nums2[:n + 1]

        if len(nums3) % 2 == 0:
            result = (nums3[int(len(nums3) / 2)] + nums3[int(len(nums3) / 2 - 1)]) / 2
        else:
            result = nums3[len(nums3) // 2]
        return result
