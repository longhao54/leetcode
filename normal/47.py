# 这个很慢
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        numsd = {}
        lenth = len(nums)
        for i, v in enumerate(nums):
            numsd[i] = v
        def backtrace(t=[], used=[], lent = 0):
            if lent == lenth:
                if t not in ans:
                    ans.append(t)
                return
            for i in numsd:
                if i not in used:
                    backtrace(t+[numsd[i]], used+[i], lent+1)
        backtrace()
        return ans


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        def backtrack(combination, nums):
            if nums == []:
                return r.append(combination)
            temp = float('inf')   # 由于 已经按大小排序了  所以 temp是用来去重的 
            for i in range(len(nums)):
                if nums[i] == temp:
                    continue
                backtrack(combination + [nums[i]], nums[:i] + nums[i+1:])
                temp = nums[i]
        backtrack([], nums)
        return r 
