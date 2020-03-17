class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        start = 0
        while start < len(s):
            if len(s[start:start+k]) >= k:
                p = s[start:start+k][::-1]
                s = s[0:start] + p + s[start+k:]
            else:
                p = s[start:][::-1]
                s = s[0:start] + p
            start += 2*k
        return s
