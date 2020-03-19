class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c = set()
        l = len(matrix[0])
        for li,line in enumerate(matrix):
            ck = False
            for ri, v in enumerate(line):
                if v == 0:
                    c.add(ri)
                    ck = True
            if ck:
                matrix[li] = [0] * l  
        l1 = len(matrix)
        for i in c:
            for j in range(l1):
                matrix[j][i] = 0
