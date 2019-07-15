class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A> B:
            m,s = A,B
        else:
            m,s = B,A
        if A > B:
            sa, sb = "a","b"
        else:
            sa, sb = "b", "a"
        ans = ""
        for i in range(0,m):
            ans += sa
            if i % 2 ==0:
                if s >=2:
                    ans += "bb"
                elif s == 1:
                    ans += "b"
                s -= 2
        return ans
