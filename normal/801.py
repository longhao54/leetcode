class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        cost = [0 ,1]
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                if A[i] > B[i - 1] and B[i] > A[i - 1]:
                    cost = [min(cost), min(cost) + 1]
                else:
                    cost[1] += 1
            else:
                cost = [cost[1],cost[0] + 1]
        return min(cost)
