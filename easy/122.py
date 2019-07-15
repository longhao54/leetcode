'''

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for index,num in enumerate(prices[1:]):
            if num > prices[index]:
                ans += num -prices[index]
        return ans

a = Solution()
print(a.maxProfit([7,1,5,3,6,4,10,11]))