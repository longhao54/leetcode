class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return 
        self.matrix = matrix
        for index, value in enumerate(matrix[0][1::]):
            matrix[0][index+1] = matrix[0][index] + value
        for index, temp in enumerate(matrix[1::]):
            for index_2, value in enumerate(temp):
                if index_2 == 0:
                    matrix[1+index][0] = value + matrix[index][0]
                else:
                    matrix[1+index][index_2] = value + matrix[index][index_2] + matrix[index+1][index_2 -1 ] - matrix[index][index_2-1]
                
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 + col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0 and col1 != 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        elif row1 != 0 and col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]
        else:
            return self.matrix[row2][col2] + self.matrix[row1-1][col1-1] - self.matrix[row2][col1-1] - self.matrix[row1-1][col2]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
