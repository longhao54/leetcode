class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(['0' if x == '1' else '1' for x in bin(num)[2:]]),2)

    def  fast(self, num):
        res = ''
        if num == 0:
            return 1
        while num!=0:
            res = str((num%2)^1)+res
            num = num//2
            
        return int(res,2)
