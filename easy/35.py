'''

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。  应该是要用二分查找法做才对

'''


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in nums:
            if i == target:
                return nums.index(i)
            elif target > i :
                continue
            else:
                return nums.index(i)
        return len(nums)


# 别人的
class Solution_other:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_len = len(nums)
        i = 0
        j = nums_len - 1

        mid = int((i + j) / 2)
        while True:
            if j < 0:
                return 0
            if i >= nums_len:
                return i

            if i > j:
                return i + 1 if nums[i] < target else i

            mid = int((i + j) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

a = Solution()
print(a.searchInsert([1,3,5,6],9))