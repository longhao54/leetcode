class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0
        l = len(grid[0])
        lenth = len(grid) 
        for i in range(len(grid)):
            for j in range(l):
                t = grid[i][j]
                if t == 0:
                    continue
                if t == 1:
                    ans += 6
                else:
                    ans += t * 6 - (t-1) * 2
                # up
                if i != 0 and grid[i-1][j] != 0:
                    ans -= min(t, grid[i-1][j])
                # down
                if i != lenth -1 and grid[i+1][j] != 0:
                    ans -= min(t, grid[i+1][j])
                # left
                if j != 0 and grid[i][j-1] != 0:
                    ans -= min(t, grid[i][j-1])
                # right
                if j != l -1 and grid[i][j+1] != 0:
                    ans -= min(t, grid[i][j+1])
        return ans
                    
