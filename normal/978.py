class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        up = [1 for i in range(len(A))]
        low = [1 for i in range(len(A))]
        for x, v in enumerate(A[1:]):
            if v > A[x]:
                if up[x] == 1:
                    up[x+1] = low[x] +1
                else:
                    up[x+1] += 1
                
            elif v < A[x]:
                if low[x] == 1:
                    low[x+1] = up[x]+1
                else:
                    low[x+1] += 1
        return max(low+up)

