'''

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        if m == 0 and len(nums1) == 1:
            nums1[0] = nums2[0]
        elif n != 0:
            nums1[m:] = nums2
            nums1.sort()
        return nums1
        # index = 0
        # check = False
        # num = nums2.pop(0)
        # while True:
        #     try:
        #         if num <= nums1[index]:
        #             if index+1 == len(nums1)-1:
        #                 nums1[index+1:] = nums1[index:m]
        #             else:
        #                 nums1[index + 1:index + m-1] = nums1[index:m]
        #                 print(nums1)
        #             nums1[index] = num
        #             if nums2:
        #                 check = True
        #                 num = nums2.pop(0)
        #             else:
        #                 break
        #
        #         index += 1
        #         if index  == len(nums1) -1 :
        #             break
        #     except:
        #         print(index)
        #         break
        # if check:
        #     nums2.insert(0,num)
        #     if len(nums2) == 1:
        #         nums1[-1] = num
        #     else:
        #         lenth = len(nums2)
        #         lenth1= len(nums1)
        #         nums1[lenth1-lenth:] = nums2
        # return nums1

a = Solution()
# print(a.merge([1],1,[],0))
# print(a.merge([0],0,[1],1))
print(a.merge([0,0,0,0,0],0,[1,2,3,4,5],5))
# print(a.merge([1,2,3,0,0,0],3,[2,5,6],3))
# print(a.merge([2,0],1,[1],1))
# print(a.merge([1,1,2,7,0,0,0,0,0],4,[2,3,6,8,8],5))
