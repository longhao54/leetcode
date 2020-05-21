from collections import defaultdict
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        tmp = defaultdict(list)
        for x, y in relation:
            tmp[x].append(y)
        
        ans = 0
        def check(start=0, count=k):
            nonlocal ans, n
            if count == 0:
                if start == n-1:
                    ans += 1
                return ""
            for i in tmp[start]:
                check(i, count-1)
        
        check()
        return ans
