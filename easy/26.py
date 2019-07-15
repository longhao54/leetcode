'''

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

'''



# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         if len(nums) == 1:
#             return 1
#         index = 0
#         check = False
#         while True:
#             try:
#                 number = nums[index]
#                 if number == nums[index+1]:
#                     nums.remove(number)
#                     check = True
#                 else:
#                     index += 1
#             except:
#                 index +=1 if index else 0
#                 if check and index == 0:
#                     index += 1
#                 break
#         return(index)

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l<=1:
            return l
        index = 0
        for i in range(0,l-1):
            if nums[i]!=nums[i+1]:
                nums[index+1]=nums[i+1]
                index+=1
        print(nums)
        return index+1


a = Solution()
print(a.removeDuplicates([1,1,2,2,3,4,5,5,5,6]))