class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        ans = 0
        arr.sort()
        t = 5000
        for i in arr:
            if i <= t:
                ans += 1
                t -= i
            else:
                break
        return ans
