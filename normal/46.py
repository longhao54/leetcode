class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        lenth = len(nums)
        numsd = {}
        for index, value in enumerate(nums):
            numsd[index] = value
        def backtrace(t=[], index=0, lent = 0):
            if lent == lenth:
                ans.append(t)
            for i in numsd:
                if nums[i] not in t:
                    backtrace(t+[numsd[i]], index+1, lent+1)
        backtrace()
        return ans
