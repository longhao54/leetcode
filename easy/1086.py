from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ans = defaultdict(list)
        for i in items:
            k, v = i
            ans[k].append(v)
        t = []
        for k, v in ans.items():
            v.sort()
            t.append([k, sum(v[-1:-6:-1])//5])
        return t
