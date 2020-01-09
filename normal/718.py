from collections import defaultdict


# 这种方式会超时
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dictB = defaultdict(list)
        for i, v in enumerate(B):
            dictB[v].append(i)

        ans = 0
        lenA, lenB = len(A), len(B)
        for i, v in enumerate(A):
            for k in dictB[v]:
                t = 0
                while i+t < lenA and k+t < lenB and A[i + t] == B[k + t]:
                    t += 1
                ans = max(ans, t)
        return ans


# 动态规划
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        ans = [ [0] * (len(B)+1) for _ in range(len(A)+1) ]
        for i, v1 in enumerate(A):
            for j, v2 in enumerate(B):
                if v1 == v2:
                    ans[i+1][j+1] = ans[i][j]+1
        return max([max(i) for i in ans])            
