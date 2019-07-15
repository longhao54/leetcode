class Solution:
    def lastStoneWeightII(self, stones):
        lenth = len(stones)
        while lenth > 1:
            stones.sort()
            a = stones.pop() - stones.pop()
            if a != 0:
                stones.append(a)
                lenth -= 1
            else:
                lenth -= 2
        if lenth == 1:
            return stones[0]
        else:
            return 0

a = Solution()
#print(a.lastStoneWeightII([2,7,4,1,8,1]))
print(a.lastStoneWeightII([31,26,33,21,40]))
