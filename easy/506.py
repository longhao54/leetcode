'''

相对名次

'''

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return ["Gold Medal"]
        Nums = nums.copy()
        nums.sort()
        nums = nums[::-1]
        temp_dict = {}
        for index, value in enumerate(nums):
            if index + 1 == 1:
                temp_dict[value] = "Gold Medal"
            elif index + 1 ==2:
                temp_dict[value] = "Silver Medal"
            elif index + 1 ==3:
                temp_dict[value] = "Bronze Medal"
            else:
                temp_dict[value] = str(index + 1)
        for index, value in enumerate(Nums):
            Nums[index] = temp_dict[value]
        return Nums


        # 与我写的效率同样100%的示例代码
        # l = sorted(nums)
        # l = l[::-1]
        # maps = {}
        # for i in range(len(nums)):
        #     maps[l[i]] = i + 1
        # for j in range(len(nums)):
        #     if maps[nums[j]] == 1:
        #         nums[j] = 'Gold Medal'
        #     elif maps[nums[j]] == 2:
        #         nums[j] = 'Silver Medal'
        #     elif maps[nums[j]] == 3:
        #         nums[j] = 'Bronze Medal'
        #     else:
        #         nums[j] = str(maps[nums[j]])
        # return nums

a = Solution()
print(a.findRelativeRanks([10,3,8,9,4]))
print(a.findRelativeRanks([5,4,3,2,1]))
print(a.findRelativeRanks([1,2]))