class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        start, end = 0, len(mat)-1
        for i in range(len(mat)):
            ans += mat[start][start] + mat[i][end]
            start += 1
            end -= 1
    
        if len(mat) %2 != 0:
            ans -= mat[start//2][start//2]
        
        return ans
