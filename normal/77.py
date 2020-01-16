class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [ i for i in range(1, n+1)]
        ans = []
        def backtrace(nums=nums, t=[]):
            if len(t) == k:
                ans.append(t)
            for i, v in enumerate(nums):
                backtrace(nums[i+1:], t+[v])
        backtrace()
        return ans
