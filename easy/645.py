'''

错误的数

'''


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Sum1 = sum(nums)
        Sum2 = sum(set(nums))
        lenth = len(nums)
        num = Sum1 - Sum2
        Sum3 = (1 + lenth) * lenth // 2 if lenth % 2 == 0 else (1 + lenth) * lenth // 2 + (1 + lenth) // 2
        print(lenth, Sum3)
        not_in_nums = Sum3 - Sum2
        return (num, not_in_nums)

a = Solution()
print(a.findErrorNums([3,2,2]))