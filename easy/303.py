'''

给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

'''

# 这个是我写的渣渣答案 耗时1200ms
# class NumArray:
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
#
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         a = self.nums[i:j + 1]
#         return sum(a)
#
#
#
#         # Your NumArray object will be instantiated and called as such:
#         # obj = NumArray(nums)
#         # param_1 = obj.sumRange(i,j)

class NumArray:  # 最快的 O(n) 方法）
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = []
        temp = 0
        for i in nums:
            temp += i
            self.sums.append(temp)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]