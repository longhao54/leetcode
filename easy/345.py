class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) -1
        s = list(s)
        for i in range(0, len(s)):
            if i > right:
                break
            if s[i] in "aeiouAEIOU":
                while i < right:
                    if s[right] in "aeiouAEIOU":
                        s[right], s[i] = s[i], s[right]
                        right -= 1
                        break
                    right -= 1
        return "".join(s)
                    
