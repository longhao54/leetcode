class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        cnt = s // 2
        memo = [False] * (cnt + 1)
        for i in range(0, cnt + 1):
            memo[i] = (nums[0] == i)
        for i in range(1, len(nums)):
            for j in range(cnt, nums[i] - 1, -1):
                memo[j] = memo[j] or memo[j - nums[i]]
        return memo[cnt]
