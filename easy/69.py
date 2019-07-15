'''

x 的平方根

'''


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        '''
        最佳答案
        return int(x**0.5)
        '''

        if x <=0:
            return x
        start = 10**(len(str(x))/2 -1)
        print(start)
        for i in range(int(start),x+1):
            if i*i > x:
                return i-1

a = Solution()
print(a.mySqrt(1723648389))