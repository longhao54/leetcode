class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrace(t=[], nums=nums):
            ans.append(t)
            for i, v in enumerate(nums):
                backtrace(t+[v], nums[i+1:])
        backtrace()
        return ans
