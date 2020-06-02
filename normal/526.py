class Solution:
    def countArrangement(self, N: int) -> int:
        result = 0
        nums = [i for i in range(1, N + 1)]
        def helper(nums, ind, arr):
            if not nums:
                nonlocal result
                result += 1
                return
            for i, num in enumerate(nums):
                if ind % num == 0 or num % ind == 0:
                    helper(nums[:i] + nums[i + 1:], ind + 1, arr + [num])
        helper(nums, 1, [])
        return result
