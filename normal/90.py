class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrace(nums=nums, t=[]):
            ans.append(t)
            for i, v in enumerate(nums):
                if t+[v] not in ans:
                    backtrace(nums[i+1:], t+[v])
        backtrace()
        return ans
