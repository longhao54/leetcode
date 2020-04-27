class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        one = s.count("1")
        zero = len(s) - one
        if s[0] == "1":
            l, r = 0, one-1
        else:
            l, r = 1, one
        ans = l + r
        for i in s[1:-1]:
            if i == "1":
                r -= 1
            else:
                l += 1
            ans = max(ans, r+l)
        return ans
