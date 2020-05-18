class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dp = [[0 for j in range(n)] for i in range(n)]
        for length in range(1, n + 1, 1):
            for i in range(0, n - length + 1, 1):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = nums[i]
                elif length == 2:
                    dp[i][j] = nums[i] - nums[j] if nums[i] >= nums[j] else nums[j] - nums[i]
                else:
                    dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        if dp[0][n-1] >= 0:
            return True
        else:
            return False
