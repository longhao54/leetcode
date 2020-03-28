class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return matrix
        lx, ly = len(matrix), len(matrix[0])
        # 往右下
        ans = [[float("inf")] * ly for i in range(lx)]
        for x, line in enumerate(matrix):
            for y, v in enumerate(line):
                if v == 0:
                    ans[x][y] = 0
                if x > 0:
                    ans[x][y] = min(ans[x][y], ans[x-1][y]+1)
                if y > 0:
                    ans[x][y] = min(ans[x][y], ans[x][y-1]+1)
        # 往左上
        for x in range(lx-1, -1, -1):
            for y in range(ly-1, -1, -1):
                if x < lx -1:
                    ans[x][y] = min(ans[x][y], ans[x+1][y]+1)
                if y < ly -1:
                    ans[x][y] = min(ans[x][y], ans[x][y+1]+1)
        return ans
