class Solution:
    def maxA(self, N: int) -> int:
        ans = [0, 1]
        for i in range(2, N+1):
            ans.append( max(ans[j] * (i-j-1) for j in range(i-1)))
            ans[-1] = max(ans[-1], ans[-2]+1)
        return ans[-1]
