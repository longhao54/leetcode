class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Nums = set(nums)
        count = 0
        if not nums:
            return 0
        if k < min(nums) and k != 0:
            return 0
        if k != 0:
            for i in Nums:
                if i + k in Nums:
                    count += 1
        else:
            for i in Nums:
                if nums.count(i) >= 2:
                    count += 1
        return count
