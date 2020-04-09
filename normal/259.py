class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        self.nums = nums
        right = len(nums)-1
        nums.sort()
        ans = 0
        for i in range(right-1):
            ans += self.check(i+1, right, target - nums[i])
        return ans
         
        
    def check(self, left, right, target):
        ans = 0
        while left < right:
            if self.nums[left] + self.nums[right] >= target:
                right -= 1
            else:
                ans += right-left 
                left += 1
        return ans
