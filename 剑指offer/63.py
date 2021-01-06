class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_prices = prices[0]
        ans = 0
        for i in prices[1:]:
            if i > min_prices:
                ans = max(ans, i-min_prices)
            else:
                min_prices = i
        return ans
