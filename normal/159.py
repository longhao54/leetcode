class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        right = 0
        w = ""
        check = set()
        c = 0
        ans = 0
        while left < len(s) and right < len(s):
            if len(check) <= 2:
                t = s[right]
                w += t
                check.add(t)
                right += 1
                ans += 1
                if len(check) <= 2:
                    c = max(ans, c)
            else:
                w = w[1:]
                t = s[left]
                if t not in w:
                    check.remove(t)
                ans -= 1
                left += 1
        return c
