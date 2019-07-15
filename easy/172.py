'''

给定一个整数 n，返回 n! 结果尾数中零的数量。

'''


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n//5
            n = n// 5
        return count

a = Solution()
print(a.trailingZeroes(10))