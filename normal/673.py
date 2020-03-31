class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lenth = [0] * len(nums)
        count = [1] * len(nums)
        for i, v in enumerate(nums):
            for j in range(i):
                if nums[j] < v:
                    if lenth[j] >= lenth[i]:
                        lenth[i] = lenth[j]+1
                        count[i] = count[j]
                    elif lenth[j] + 1== lenth[i]:
                        count[i] += count[j]
        m = max(lenth)
        return sum(num for i, num in enumerate(count) if lenth[i] == m)
