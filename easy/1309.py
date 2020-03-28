class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        for i in s:
            if i == "#":
                t1, t2 = ans[-1], ans[-2]
                ans = ans[:-2]
                p1 = ord(t1) - ord("a") +1
                p2 = ord(t2) - ord("a") +1
                ans += chr(ord("a") + p2*10+p1 -1)
            else:
                ans += chr(ord("a") + int(i) - 1)
        return ans
