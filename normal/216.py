class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        nums = [ i for i in range(1,10) ]
        def backtrace(t=[], n=n, k=k, nums=nums):
            if n == 0 and len(t) == k:
                ans.append(t)
                return ""
            elif len(t) > k-1:
                return ""
            for i, v in enumerate(nums):
                backtrace(t+[v], n-v, k, nums[i+1:])

        backtrace()
        return ans 
