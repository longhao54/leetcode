'''

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True

'''

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #弱智方法
        # if num == 1:
        #     return True
        # for i in range(1, num):
        #     if i * i == num:
        #         return True
        #     elif i * i > num:
        #         return False

        lenth = len(str(num))
        start = 10 * (lenth - 2)
        for i in range(start, lenth):
            if i * i == num:
                return True
            elif i * i > num:
                return False