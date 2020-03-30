class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        ans = 0
        for i in range(0, len(A[0])):
            for j in range(1,len(A)):
                if A[j][i] < A[j-1][i]:
                    ans += 1
                    break
        return ans
