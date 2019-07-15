class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        temp = set(nums)
        if target not in temp:
            return [-1, -1]
        return [nums.index(target), len(nums) - nums[::-1].index(target) -1 ]


    def binary_search(self, nums, target, right=False):
        lo, hi = 0, len(nums)
        while lo < hi:
            #print("Trying to find %d at [%d, %d]" % (target, lo, hi))
            mid = (lo + hi) // 2
            #print("Comparing target %d with mid %d[#%d]" % (target, nums[mid], mid))
            if target > nums[mid] or (right and target == nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def fast(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binary_search(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = self.binary_search(nums, target, True) - 1
        return [left, right]
