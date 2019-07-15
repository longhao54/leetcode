'''

猜数字大小

'''

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        Min = 0
        Max = n+1
        if n <= 1:
            return n
        while Min < Max:
            mid = (Min+Max) // 2 
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                Max = mid
            else:
                Min = mid
