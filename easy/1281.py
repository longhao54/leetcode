class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        t1 = 1
        t2 = 0
        while n > 0:
            tmp = n % 10
            n //= 10
            t1 *= tmp
            t2 += tmp
        return t1-t2
