# 弱智方法
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        w, p = {}, {}
        for d,pri in zip (difficulty, profit):
            w[d] = 1
            if d in p:
                p[d] = max(pri, p[d])
            else:
                p[d] = pri
        
        difficulty.sort()
        m = p[difficulty[0]]
        d1 = difficulty[0]
        while d1-1 >= 1:
            p[d1-1] = 0
            d1 -= 1
        m1 = max(worker)
        for v in difficulty[1:]:
            t = v
            while t-1 not in p:
                p[t-1] = m
                t -= 1
            m = max(p[v], m)
            p[v] = m
        for i in range(difficulty[-1]+1, m1+1):
            p[i] = m
        ans = 0
        for i in worker:
            ans += p[i]
        return ans

#官方方法
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = zip(difficulty, profit)
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans

