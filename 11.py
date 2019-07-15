'''
最大桶
输入: [1,8,6,2,5,4,8,3,7]
输出: 49

'''

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sum = []

        t_dict = {}
        s_dict = {}
        for i, num in enumerate(height):
            t_dict[i] = num