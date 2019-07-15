'''

给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

'''

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        while True:
            Sum = 0
            for i in num:
                Sum += int(i)
            num = list(str(Sum))
            if Sum < 10:
                return Sum

a = Solution()
print(a.addDigits(38))