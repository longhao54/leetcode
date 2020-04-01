class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start= 0
        end = 3
        ans = 0
        
        while start < len(s)-2:
            p = s[start:end]
            if "a" in p and "b" in p and "c" in p:
                ans += len(s)-end+1  # 这块没太想明白
                start += 1
            else:
                end += 1
            if end > len(s):
                break
        return ans
