from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        t = defaultdict(int)
        for i in arr:
            t[i] += 1
        s = set()
        for v in t.values():
            s.add(v)
        return len(s) == len(t)
