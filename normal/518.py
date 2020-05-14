class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = [0] * (amount+1)
        ans[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                ans[x] += ans[x - coin]
        return ans[amount]
