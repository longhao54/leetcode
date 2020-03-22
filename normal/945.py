class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        m = { i:0 for i in range(min(A), min(A)+ max(A) + len(A)+1)}
        for i in A:
            m[i] += 1
        t1, t2 = [], []
        for k, v in m.items():
            if v == 0:
                t1.append(k)
            elif v > 1:
                t2 += [k] * (v-1)
        ans = 0
        t1.sort()
        t2.sort()
        for i in t2:
            while t1:
                p = t1.pop(0)
                if p > i:
                    ans += p-i
                    break
        return ans
