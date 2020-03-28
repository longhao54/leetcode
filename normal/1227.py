class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        dp[i] = 1 / i + (i - 2) / i * dp[i - 1]
        return 1.0 if n == 1 else 0.5
