class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        moved = []
        if not matrix:
            return 0
        if "1" in matrix[0] or len(matrix) > 1 and "1" in matrix[1]:
            ans = 1
        for x, value in enumerate(matrix[1:]):
            for y, v in enumerate(value[1:]):
                if v == "1":
                    t = min(int(matrix[x][y]), int(matrix[x+1][y]), int(matrix[x][y+1])) +1
                    matrix[x+1][y+1] = str(t)
                    ans = max(ans, t)
        return ans * ans
