class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = set(nums)
        S = sum(nums)
        count = 0
        for i in b:
            count += i*2
        return count - S
        

    def fast(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            n = m + 1 if m % 2 == 0 else m - 1
            if nums[m] != nums[n]:
                r = m
            else:
                l = m + 1
        return nums[l]
        
