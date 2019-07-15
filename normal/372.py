class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
#        a^b %c == a^(b%phi(c))  phi(c)是欧拉函数，表示小于c的和c互质的数的个数
        sum = 0
        for i in b:
            sum = sum * 10 + i
        return pow(a, sum, 1337)
