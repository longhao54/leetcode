class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(n):
            nums.append(start+2*i)
        ans=nums[0]
        for i in range(1,n):
            ans=ans^nums[i]
        return ans
