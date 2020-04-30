class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        while len(nums)>0:
            result.append(nums.pop())
            if sum(result) > sum(nums):
                return result
