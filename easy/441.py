class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        Sum = 0
        count = 1
        while Sum <= n:
            Sum += count
            count += 1
        return count-2
