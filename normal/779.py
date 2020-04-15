class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def check(n, k):
            if n == 1:
                return 0
            c = check(n-1, k//2 + k %2)
            if c == 1:
                if k%2 ==0:
                    return 0
                else:
                    return 1
            if c ==0:
                if k % 2 == 0:
                    return 1
                else:
                    return 0
        ans = check(N, K)
        return ans
