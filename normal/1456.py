class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        tmp = 0
        last = ""
        check = "aeiou" 
        ans = 0
        for i, v in enumerate(s):
            if v in check:
                tmp += 1
            if i >= k and s[i-k] in check:
                tmp -= 1
            ans = max(ans, tmp)
        return ans
