class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        c = {"xy":0, "yx":0}
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c[s1[i]+s2[i]] += 1
        if sum(c.values()) % 2 != 0:
            return -1
        ans = 0
        ans += c["xy"] // 2 + c["yx"] // 2
        if c["xy"] % 2 == 1:
            ans += 2
        return ans
