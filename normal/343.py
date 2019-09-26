class Solution:
    def integerBreak(self, n: int) -> int:
        ans = [1] * (n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                ans[i] = max(ans[i], ans[i-j]*j, (i-j)*j)
        return ans[-1]
