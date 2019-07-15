class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        line, row = [], []
        for index, i in enumerate(matrix):
            if 0 in i:
                line.append(index)
                 
