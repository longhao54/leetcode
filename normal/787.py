#  深度优先 中间重复的方法太多了 
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        ans = float("inf")
        if src == dst:
            return 0
        dic = defaultdict(list)
        for k, v , value in flights:
            dic[k].append([v, value])
        def check(start, value=0, count=-1):
            nonlocal ans, K, dst
            if count > K:
                return ""
            if start == dst:
                ans = min(ans, value)
                return ""
            for nxt, val in dic[start]:
                check(nxt, value+val, count + 1)
        
        check(src)
        return ans if ans != float("inf") else -1


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        best = {}
        pq = [(0, 0, src)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K+1 or cost > best.get((k, place), float('inf')): continue
            if place == dst: return cost

            for nei, wt in graph[place].items():
                newcost = cost + wt
                if newcost < best.get((k+1, nei), float('inf')):
                    heapq.heappush(pq, (newcost, k+1, nei))
                    best[k+1, nei] = newcost

        return -1
