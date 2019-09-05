class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = dict()
        lenth = cost.__len__()
        if lenth <=1:
            return 0
        elif lenth == 2:
            return min(cost[0], cost[1])
        dp[0] = cost[0]
        dp[1] = cost[1]
        for index, i in enumerate(cost[2:]):
            dp[index+2] = min(dp[index]+i, dp[index+1]+i)
        return min(dp[lenth-1], dp[lenth-2]) 
        
