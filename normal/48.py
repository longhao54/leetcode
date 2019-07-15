class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1):
            for j in range(n-i-1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][n-i-1]
                matrix[n-j-1][n-i-1] = tmp
        """再对调行，行数相加等于n-1"""
        for i in range(n//2):
            tmp = matrix[i]
            matrix[i] = matrix[n-1-i]
            matrix[n-i-1] = tmp
