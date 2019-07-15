'''
给定一个 32 位有符号整数，将整数中的数字进行反转。
321
123
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        s = s[::-1] if s[0] != "-" else s[-1:0:-1]
        s = int(s) if x>0 else -int(s)
        if s > 2**31 or s < -2**31:
            return 0
        else:
            return s

a = Solution()
print(a.reverse(1534236469))
