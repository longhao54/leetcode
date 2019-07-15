class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new = sorted(nums1) + sorted(nums2)
        m = len(new) / 2
        if m % 2 == 0:
            return new[int(m)]
        else:
            return (new[int(int(m)) - 1] + new[int(int(m)) + 1]) / 2

a = Solution()
print(a.findMedianSortedArrays([3],[-2,-1]))