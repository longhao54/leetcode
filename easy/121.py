'''

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 这个方法 时间复杂度太高 超出计算时间
        # if len(prices) <=1:
        #     return 0
        # ans = [0]
        # for index, num in enumerate(prices[0:-1]):
        #     Max =  max(prices[index+1:])
        #     if Max >= num:
        #         ans.append(Max-num)
        # return max(ans)

        max = 0
        min = prices[0] if prices else 0
        for i in prices:
            if i < min :
                min = i
            else:
                ans = i - min
                max = max if max > ans else ans
        return max


a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))