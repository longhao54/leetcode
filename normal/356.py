from collections import defaultdict
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        t = defaultdict(set)
        m, s = float("-inf"), float("inf")
        for i in points:
            k, v = i
            t[k].add(v)
            m = max(m, k)
            s = min(s, k)
        mid = (m + s) / 2
        checked = set()
        for k, v in t.items():
            if k in checked:
                continue
            if k > mid:
                p = mid - abs(mid-k)
            elif k < m:
                p = mid + abs(mid-k)
            else:
                continue
            v2 = t[p]
            if v2 != v:
                return False
            checked.add(p)
            checked.add(k)
        return True
