class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        ans = [ -1 ] * min(coins) + [0] * (amount-min(coins)+1)
        for i in range(min(coins), amount+1):
            if i in coins:
                ans[i] = 1
            else:
                
                temp = []
                for j in coins:
                    if i - j >= 1 and ans[i-j] != -1:
                        temp.append(ans[i-j] +1)
                if temp:
                    ans[i] = min(temp)
                else:
                    ans[i] = -1
        return ans[-1]
