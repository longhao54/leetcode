'''

非递减序列

'''

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Index = -1
        last=nums[0]
        for index,i in enumerate(nums):
            if i < last:
                Index = index
                break
            last = i
        tempA = nums.copy()
        tempB = nums.copy()
        tempA.pop(index)
        tempB.pop(index-1)
        return tempA == sorted(tempA) or tempB == sorted(tempB)

    def fast(self, nums):
        changecount=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                changecount+=1
                if(i-1<0 or nums[i+1]>=nums[i-1]):
                    nums[i]=nums[i+1]
                else:
                    nums[i+1]=nums[i]
            if changecount>1:
                return False
        return True
        

a = Solution()
print(a.checkPossibility([2,3,3,2,4]))
