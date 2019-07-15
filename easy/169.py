'''

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。


'''


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set_nums = set(nums)
        # temp_dict = {}
        # lenth = len(nums)//2
        # for i in set_nums:
        #     temp_dict[i] = 0
        # for i in nums:
        #     temp_dict[i] += 1
        # print(temp_dict)
        # for k, v in temp_dict.items():
        #
        #     if v > lenth:
        #         return k
        nums.sort()
        lenth = len(nums)//2
        for index, num in enumerate(nums):
            if num == nums[index+lenth]:
                return num

    def other_majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = None
        for i in nums:
            if count == 0:
                temp = i
            count += 1 if i == temp else -1
        return temp



a = Solution()
print(a.majorityElement([3,2,3]))