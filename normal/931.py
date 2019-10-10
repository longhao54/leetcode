class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        lenth = A[0].__len__()
        for i, j  in enumerate(A[1::]):
            for index, value in enumerate(j):
                if index == 0:
                    A[i+1][index] += min(A[i][index], A[i][index+1])
                elif index == lenth-1:
                    A[i+1][index] += min(A[i][index], A[i][index-1])
                else:
                    A[i+1][index] += min(A[i][index], A[i][index+1], A[i][index-1])
        return min(A[-1])
