class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i, v in enumerate(s[::-1]):
            t = ord(v)-ord("A") +1 
            ans += t * (26**i)
        return ans
