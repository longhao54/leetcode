'''

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。


'''

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_len = len(nums)
        if nums_len <= 1:
            return False
        nums_dict = {}
        for i in range(nums_len):
            if nums[i] in nums_dict:
                if i-nums_dict[nums[i]] <= k:
                    return True
            nums_dict[nums[i]] = i
        return False
