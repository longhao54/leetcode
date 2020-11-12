class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows, cols = [], []
        output = 0
        for row in mat:
            rows += [sum(row)]

        for i in range(m):
            res = 0
            for j in range(n):
                res += mat[j][i]
            cols += [res]
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    output += 1

        return output

