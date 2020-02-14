from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans = set()
        t = defaultdict(list)
        for i in points:
            x, y = i
            p = x*x+y*y
            t[p].append(i)
            ans.add(p)
        re = []
        lenth = 0

        ans = list(ans)
        ans.sort()
        for i in ans:
            for v in t[i]:
                re.append(v)
                lenth += 1
                if lenth == K:
                    return re
        return re
