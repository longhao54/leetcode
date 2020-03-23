class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        t = sorted(heights)
        l = len(t)
        ans = 0
        for i in range(l):
            if t[i] != heights[i]:
                ans+=1
        return ans
