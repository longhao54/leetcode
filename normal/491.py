# 特别慢的做法
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def check(l1, now):
            lenth = len(l1)
            if lenth > 1 and l1[-1] < l1[-2]:
                return ""
            if lenth > 1 and l1 not in ans:
                ans.append(l1)
            if not now:
                return ""
            for i, v in enumerate(now):
                check(l1+[v], now[i+1:])
        
        for i, v in enumerate(nums):
            check([v], nums[i+1:])
        return ans
