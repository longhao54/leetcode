class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) -1 
        while start < end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return True
            elif nums[middle] > target:
                start = middle
            else:
                end = middle

        return False
