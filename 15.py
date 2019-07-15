'''
三数之和
nums = [-1, 0, 1, 2, -1, -4]，
找出所有 三个数相加和为0 的组合
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''

# def check(nums1, nums2, check=False):
#     Sum = []
#     Sum_set = set()
#     for i, num in enumerate(nums1):
#         for num2 in nums1[i+1:]:
#             add = -sum([num, num2])
#             if add in Sum_set:
#                 continue
#             if add in nums2 :
#                 a = [num, num2, add]
#                 a.sort()
#                 if a not in Sum:
#                     Sum.append(a)
#             else:
#                 Sum_set.add(add)
#         if check:
#             if -num in nums2:
#                 a = [num, -num, 0]
#                 if a not in Sum:
#                     Sum.append(a)
#     return Sum
#
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         Sum = []
#         lt_0, gt_0, eq_0  = [], [], []
#
#         # lenth = len(nums)
#         # if lenth <= 2:
#         #     return []
#         # elif lenth == 3:
#         #     if sum(nums) == 0:
#         #         return [nums]
#
#         gt,lt, eq = 0, 0, 0
#         for i in nums:
#             if i > 0:
#                 gt_0.append(i)
#                 gt+=1
#             elif i < 0:
#                 lt_0.append(i)
#                 lt+=1
#             else:
#                 eq_0.append(i)
#                 eq+=1
#
#         # if (not gt_0 or not lt_0) and not eq_0:
#         #     return []
#
#         g,l =set(gt_0), set(lt_0)
#
#         Check = False
#         if eq:
#             Check = True
#
#         if lt >=1:
#             Sum += check(lt_0, g, Check)
#         if gt >=1:
#             Sum += check(gt_0, l)
#         if eq >= 3:
#             Sum.append([0,0,0])
#
#         return Sum

def check(nums1, nums2, check=False):
    Sum = []
    C_check = {}
    for i in nums1:
        if check:
            if -i in nums2:
                a = [i, -i, 0]
                Sum.append(a)

        for j in nums2:
            S = 0 - sum([i,j])
            a = sorted([i, j, S])
            string = "{}+{}+{}".format(a[0],a[1], a[2])
            if string not in C_check:
                C_check[string]=0
            else:
                continue
            if S in nums2:
                if S == j and nums2[j] == 0:
                    continue
                Sum.append(a)
            if S in nums1:
                if S == i and nums1[i] == 0 :
                    continue
                Sum.append(a)
    return Sum


class Solution:
    def threeSum(self, nums):
        Sum = []
        lt_0, gt_0, eq_0, eq_check = {}, {}, {}, 0
        nums.sort()
        for i in nums :
            if i > 0:
                if i in gt_0:
                    gt_0[i] = 2
                else:
                    gt_0[i] = 0
            elif i < 0:
                if i in lt_0:
                    lt_0[i] = 2
                else:
                    lt_0[i] = 0
            else:
                eq_0[0] = 0
                eq_check += 1

        Check = True if eq_check else False
        if eq_check >= 3:
            Sum.append([0,0,0])

        Sum += check(lt_0, gt_0, Check)

        # if len(gt_0) >= 1:
        #     Sum += check(gt_0, lt_0)

        # print(gt_0, lt_0)
        return Sum

a = Solution()
# nums=[1,1,-2]
# nums = [-1, 0, 1, 2, -1, -4]
# nums = [-2,0,1,1,2]
# nums = [-1,0,1,2,-1,-4]
nums = [-1,0,1,2,-1,-4]
print(a.threeSum(nums))