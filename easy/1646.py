# 比较慢
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [0, 1] + [0] * n
        start = 0
        ans = 1
        while start <= n // 2:
            dp[2*start] = dp[start]
            dp[2*start+1] = dp[start] + dp[start+1]
            start += 1
        return max(dp[0:-1])
