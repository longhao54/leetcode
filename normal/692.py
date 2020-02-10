from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        t = defaultdict(int)
        t1 = defaultdict(list)
        for i in words:
            t[i] += 1
        ans = []
        c = set()
        for key, v in t.items():
            t1[v].append(key)
            c.add(v)
        for key, v in t1.items():
            v.sort()
            t1[key] = v[::-1]
        c = list(c)
        c.sort()
        while len(ans) < k:
            m = c[-1]
            if t1[m]:
                ans.append(t1[m].pop())
            else:
                c.pop()
        return ans
