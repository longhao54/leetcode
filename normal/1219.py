# 很慢的方法
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = [0]
        lines = len(grid) -1
        rows = len(grid[0]) -1

    
        def temp(l, r, s, checked):
            t = grid[l][r]
            if  t != 0 and [l, r] not in checked:
                backtrace(l, r, s+t, checked+[[l, r]])
                return True
            return False

        def backtrace(line=0, row = 0, s=0, checked = []):
            moved = False
            #up
            if line != 0:
                l, r = line-1, row
                moved = temp(l, r, s, checked)
            if line != lines:
                l, r = line+1, row
                moved = temp(l, r, s, checked)
            #left
            if row != 0:
                l, r = line, row-1
                moved = temp(l, r, s, checked)
            #right
            if row != rows:
                l, r = line, row+1
                moved = temp(l, r, s, checked)
            if not moved:
                ans.append(s)
        for i in range(0, lines+1):
            for j in range(0, rows+1):
                if grid[i][j] != 0:
                    backtrace(i,j, grid[i][j], [[i,j]])
        return max(ans)

# 测试1  这个会比上面的代码复用的方式 稍微快一点点 应该是在调用temp的时候值传递 复制 list操作的时候多出来了耗时
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = [0]
        lines = len(grid) -1
        rows = len(grid[0]) -1


        def temp(l, r, s, checked):
            t = grid[l][r]
            if  t != 0 and [l, r] not in checked:
                backtrace(l, r, s+t, checked+[[l, r]])
                return True
            return False

        def backtrace(line=0, row = 0, s=0, checked = []):
            moved = False
            #up
            if line != 0:
                l, r = line-1, row
                t = grid[l][r]
                if  t != 0 and [l, r] not in checked:
                    backtrace(l, r, s+t, checked+[[l, r]])
                    moved = True
            if line != lines:
                l, r = line+1, row
                t = grid[l][r]
                if  t != 0 and [l, r] not in checked:
                    backtrace(l, r, s+t, checked+[[l, r]])
                    moved = True
            #left
            if row != 0:
                l, r = line, row-1
                t = grid[l][r]
                if  t != 0 and [l, r] not in checked:
                    backtrace(l, r, s+t, checked+[[l, r]])
                    moved = True
            #right
            if row != rows:
                l, r = line, row+1
                t = grid[l][r]
                if  t != 0 and [l, r] not in checked:
                    backtrace(l, r, s+t, checked+[[l, r]])
                    moved = True
            if not moved:
                ans.append(s)
        for i in range(0, lines+1):
            for j in range(0, rows+1):
                if grid[i][j] != 0:
                    backtrace(i,j, grid[i][j], [[i,j]])
        return max(ans)


# 最快答案
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] *= -1
            maxval = 0
            maxpath = {*()}
            if i > 0 and grid[i - 1][j] > 0:
                val, path = dfs(i - 1, j)
                if val > maxval:
                    maxval = val
                    maxpath = path
            if j + 1 < n and grid[i][j + 1] > 0:
                val, path = dfs(i, j + 1)
                if val > maxval:
                    maxval = val
                    maxpath = path
            if i + 1 < m and grid[i + 1][j] > 0:
                val, path = dfs(i + 1, j)
                if val > maxval:
                    maxval = val
                    maxpath = path
            if j > 0 and grid[i][j - 1] > 0:
                val, path = dfs(i, j - 1)
                if val > maxval:
                    maxval = val
                    maxpath = path
            grid[i][j] *= -1
            maxpath.add((i, j))
            return grid[i][j] + maxval, maxpath

        maxpath = {*()}
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i, j) not in maxpath and grid[i][j] > 0:
                    gold, path = dfs(i, j)
                    if gold > res:
                        res = gold
                        maxpath = path
        return res
