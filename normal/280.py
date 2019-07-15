class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums), 2):
            if i == len(nums)-1:
                break
            nums[i], nums[i+1] = nums[i+1], nums[i]

    def  fast(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return
        for i in range(1, n, 2):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            if i + 1 < n and nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
