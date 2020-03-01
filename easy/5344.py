class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, v in enumerate(nums):
            res[i] = sum(num < v for num in nums)
        return res 
