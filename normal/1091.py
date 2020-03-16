# 这个超时
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ans = float("inf")
        start = grid[0][0]
        if start != 0 or grid[-1][-1] != 0:
            return -1
        lx = ly = len(grid) - 1
        def check(x = 0, y = 0, c=1):
            nonlocal ans, lx, ly
            if x > lx or y > ly or x < 0 or y < 0:
                return ""
            if x == lx and y == ly:
                ans = min(ans, c)
                return ""
            if grid[x][y] == 0:
                check(x+1, y+1, c+1)
                check(x+1, y, c+1)
                check(x, y+1, c+1)
                check(x+1, y-1, c+1)

        check()
        return ans if ans != float("inf") else -1


# 答案
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q, n = [(0, 0, 2)], len(grid)  #第一个0代表起点，第二个0代表终点，2代表步数
        if grid[0][0] or grid[-1][-1]: #左上和右下有一个是1，说明被石头挡了
            return -1
        elif n <= 2:
            return n

	    # BFS starts
        for i, j, d in q: # 当前节点：i，j ；距离 = d
            for x, y in [(i - 1, j - 1),(i - 1, j),(i - 1, j + 1),(i, j - 1),
                        (i, j + 1),(i + 1, j - 1),(i + 1, j),(i + 1, j + 1)]:#上下左右斜上斜下斜左斜右
                if 0 <= x < n and 0 <= y < n and not grid[x][y]: #新生成的xy必须是在这个坐标系里面
                    if x == n - 1 and y == n - 1:#判断是否到终点，或者写成if x == y == n - 1:
                        return d
                    q += [(x, y, d + 1)] #不然的话把候选值放在q里面去
                    grid[x][y] = 1 #表示这个点已经被探过了赋为1就行了，不要再走回来了，然后继续BFS下去
        return -1
