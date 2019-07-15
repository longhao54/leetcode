#coding=utf-8

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0 
        now = 0
        for i in nums: 
            #这是一个动态规划问题
            #max（上家的最大利益，上家的上家的最大利益 + 当前家的利益）
            print(last, now)
            last, now = now, max(last + i, now)
        return now
        

a = Solution()
print(a.rob([1,2,3,4,5]))
