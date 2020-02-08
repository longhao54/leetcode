from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        ans = float("-inf")
        t = defaultdict(int)
        for i in A:
            t[i] += 1
        for k, v in t.items():
            if v == 1:
                ans = max(ans, k)
        return ans if ans != float("-inf") else -1
