class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 : return 0
        dp = [0] * n
        dp[0] = k
        for i in range(1, n):
            if i == 1:
                dp[i] = dp[i-1] * k
            else:
                dp[i] = (dp[i-2] + dp[i-1]) * (k - 1)
        #print(dp)
        return dp[-1]
