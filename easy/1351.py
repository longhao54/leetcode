oclass Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        if not grid:
            return 0
        l = len(grid)-1
        r = len(grid[0])-1
        def check(line = l):
            nonlocal ans, r
            t = r
            if line < 0:
                return None
            if grid[line][t] < 0:
                check(line-1)
            while t>= 0:
                if grid[line][t] < 0:
                    ans += 1
                else:
                    break
                t -= 1

        check()
        return ans
        
