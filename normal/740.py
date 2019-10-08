class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = [0] * (max(nums)+1)
        for i in nums:
            ans[i] += 1
        if len(ans) <= 2:
            return ans[-1]
        for i in range(2, len(ans)):
            ans[i] = max(ans[i-1], ans[i-2] + ans[i] * i)
        return ans[-1]
