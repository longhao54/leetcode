class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        k = k % lenth
        if k:
            nums[:] = nums[lenth-k:] + nums[0:lenth-k]
