class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if nums.__len__() <= 3:
            return max(nums)
        
        return max(self.check(nums[0:-1]), self.check(nums[1::]))
        
    def check(self, nums):   
        nums[2] += nums[0]
        for i in range(3, nums.__len__()):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2])
