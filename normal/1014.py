class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        pre_max = A[0] + 0
        for j in range(1, len(A)):
            res = max(res, pre_max + A[j] - j)
            pre_max = max(pre_max, A[j] + j)        
        return res
