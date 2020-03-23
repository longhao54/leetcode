class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        t = [ i for i in A if i < K]
        t.sort()
        ans = 0
        start, end = 0, len(t) - 1
        while start < end:
            t1, t2 = t[start], t[end]
            if t1 + t2 < K:
                start += 1
                ans = max(ans, t1+t2)
            else:
                end -= 1
        return ans if ans != 0 else -1
