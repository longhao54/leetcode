class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r, l = 0, 0
        ans = 0
        for i in s:
            if i == "R":
                r += 1
            else:
                l += 1
            if r == l:
                ans += 1
                r, l = 0, 0
        return ans
