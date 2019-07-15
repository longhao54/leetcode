'''

爬楼梯

'''


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        leetcode 上最快的
        dp = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
        '''


        if n <= 2:
            return n

        a = 1
        b = 1
        for i in range(2,n+1):
            a, b = a+b, a
        return a

a = Solution()
print(a.climbStairs(4))