class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if  not matrix or  not matrix[0]:
            return False
        line, row = 0, len(matrix[0])-1
        while line < len(matrix) and row >= 0:
            if matrix[line][row] == target:
                return True
            elif matrix[line][row] > target:
                row -= 1
            else:
                line += 1

        return False
