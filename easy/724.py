class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums[1:])
        for i in range(1,len(nums)):
            left += nums[i-i]
            right -= nums[i]
            print(i, left, nums[i-1])
            if left == right:
                return i
            if left > right:
                return -1

a = Solution()
print(a.pivotIndex([1,7,3,6,5,6]))