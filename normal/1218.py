class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        t = {}
        ans = 0
        for i in arr:
            if i-difference in t:
                t[i] = t[i-difference]+1
            else:
                t[i] = 1
            ans = max(ans, t[i])
        return ans
