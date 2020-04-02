from collections import defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        t = defaultdict(int)
        for i in arr:
            t[i] += 1
        for k, v in t.items():
            if k == v:
                ans = max(k, ans)
        return ans
