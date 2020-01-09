from collections import defaultdict

# 较慢解法  先对四个list 哈希在分组计算会快一些
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        t1, t2 = list(), list()
        for i in A:
            for j in B:
                t1.append(i+j)

        for i in C:
            for j in D:
                t2.append(i+j)


        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for v in t1:
            d1[v] += 1
        for v in t2:
            d2[v] += 1

        ans = 0
        for v in d1:
            if -v in d2:
                ans = ans + d1[v]*d2[-v]

        return ans
