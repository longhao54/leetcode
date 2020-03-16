from collections import defaultdict
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ans = 0
        if not grid:
            return ans
        lenx, leny = len(grid)-1, len(grid[0])-1
        t1 = defaultdict(list)
        def check(x, y, group):
            nonlocal leny
            if grid[x][y] == 0:
                return 0
            else:
                t1[group].append(leny * x + y)
                grid[x][y] = 0
                if y != 0:
                    check(x, y-1, group)
                if y != leny:
                    check(x, y+1, group)
                if x != lenx:
                    check(x+1, y, group)
                if x != 0:
                    check(x-1, y, group)
                return ""
        group = 0
        for x, xv in enumerate(grid):
            for y, v in enumerate(xv):
                if v == 1:
                    check(x, y, group)
                    group += 1
        t2 = defaultdict(list)
        for k, v in t1.items():
            t2[len(v)].append(v)
        for k, v in t2.items():
            if len(v) == 1:
                ans += 1
                continue
            t = len(v)
            l = len(v[0])
            for i, iv in enumerate(v[0:-1]):
                for j in v[i+1:]:
                    c = [iv[k] - j[k] for k in range(l)] 
                    if len(set(c)) == 1:
                        t -= 1
                        break
            ans += t
        return ans
