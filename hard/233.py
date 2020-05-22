class Solution:
    def countDigitOne(self, n: int) -> int:
        if n<=0:
            return 0
        count = 0
        k = 1
        while k <= n:
            count += (n//(10*k))*k + min(max(n%(10*k)-k+1, 0), k)  # 对个位也成立
            k *= 10
        return count
