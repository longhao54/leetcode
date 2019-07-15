'''

给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

'''

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # for index, num in enumerate(nums):
        #     if index != num:
        #         return index
        # return nums[-1]+1

        n = len(nums)   # 最快的方法
        return n * (n + 1) // 2 - sum(nums)