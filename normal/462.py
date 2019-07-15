class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mid = (len(nums) - 1) // 2
        result = 0
        nums = sorted(nums)
        for i in nums:
            result += abs(i - nums[mid])
        return result

    
    def twoline(self, nums):
        median = sorted(nums)[len(nums) // 2]
        return sum(abs(num - median) for num in nums)
