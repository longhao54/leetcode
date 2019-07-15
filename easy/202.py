 4,16,37,58,89,145,42,20 

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        error = [0,4,16,37,58,89,145,42,20]
        while n not in error:
            n = sum([int(i)**2 for i in list(str(n))] )
            if n == 1:
                return True
        return False
