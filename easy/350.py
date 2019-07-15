'''

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

'''


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # ans = list(set(nums1) & set(nums2))
        # correct = []
        # for i in ans:
        #     min_count = min(nums1.count(i), nums2.count(i))
        #     correct += [i for j in range(min_count)]
        # return correct

        # leetcode上最快的方式 用二维数组 在字典中确定 某数是否是重复
        dic = {}
        ans = []
        for i in nums2:
            if i in dic:
                dic[i][0] += 1
            else:
                dic[i] = [1, 0]
        for i in nums1:
            if i in dic:
                dic[i][1] += 1
        for i in dic:
            if dic[i][1] != 0:
                a = min(dic[i])
                for j in range(a):
                    ans.append(i)
        return ans