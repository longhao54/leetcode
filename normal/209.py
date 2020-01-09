class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans = float('inf')
        left = 0
        count = 0
        for i, v in enumerate(nums):
            count += v
            while count >= s:
                count -= nums[left]
                ans = min(ans, i -left +1)
                left += 1
        return ans if ans != float('inf') else 0
