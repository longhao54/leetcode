from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = defaultdict(list)
        t = []
        for v, i in enumerate(groupSizes):
            if ans[i] and len(ans[i][-1]) < i:
                ans[i][-1].append(v)
            else:
                ans[i].append([v])
        a = ans.values()
        for k, v in ans.items():
            for i in v:
                t.append(i)
        return t
