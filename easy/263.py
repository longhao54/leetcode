'''

编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3

'''

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # 下面这个方法测试用例42 就过不去
        # if num < 0:
        #     num = -num
        # return num % 6 ==0 or num %10 == 0 or num % 15 ==0 or num %4 == 0 or num %9 ==0 or num %25 ==0
        if n == 0 :
            return False
        while num % 2 == 0:
            num /= 2

        while num % 3 ==0:
            num /= 3

        while num % 5 == 0:
            num /= 5
        if num == 1:
            return True
        return False

a = Solution()
print(a.isUgly(42))  #