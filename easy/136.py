'''

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？


'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        return sum(set(nums)) * 2  - sum(nums) 
        
        '''

        nums.sort()
        lenth = len(nums)
        index = 0
        while True:
            try:
                if nums[index] == nums[index+1]:
                    index+=2
                else:
                    return nums[index]
            except:
                return nums[-1]





a=Solution()
print(a.singleNumber([4,1,2,1,2]))