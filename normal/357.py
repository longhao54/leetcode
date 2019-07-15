class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        dp=[1,9]
        n=min(n,9)
        for i in range(2,n+1):
            dp.append(dp[-1]*(10-i+1))        
        return sum(dp[:n+1])
