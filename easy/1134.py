class Solution:
    def isArmstrong(self, N: int) -> bool:
        p = list(str(N))
        l = len(p)
        p = [int(x) ** l for x in p ]
        return N == sum(p)
