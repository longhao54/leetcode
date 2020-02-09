from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        one = "ban"
        point = "lo"
        t = defaultdict(int)
        for i in text:
            if i in one:
                t[i] += 1
            elif i in point:
                t[i] += 0.5
        ans = []
        for v in t.values():
            ans.append(v)
        if len(ans) != 5:
            return 0
        return int(min(ans))
