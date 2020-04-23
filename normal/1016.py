class Solution:
    def queryString(self, S: str, N: int) -> bool:
        res = True
        if N < 2: return res
        for i in range(N>>1+1,N+1):
            s = str(bin(i))[2:]
            if s not in S:
                return False
        return res
