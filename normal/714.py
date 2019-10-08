class Solution(object):
    def maxProfit(self, prices, fee):
        '''
            cash 不持有股票的利润
            hold 持有股票时的利润
        '''
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash

