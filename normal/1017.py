class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        res = ''
        while N != 0:
            tmp = N % (-2)
            if tmp == 0:
                res = '0' + res  
            else:
                res = '1' + res  
            N = (N+tmp)/(-2)  
        return res
