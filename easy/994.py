class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dp = []
        g_count = 0
        ans = 0
        len1 = len(grid)
        if len1 == 0:
            return 0
        len2 = len(grid[0])
        if len2 == 0:
            return 0
        for line, List in enumerate(grid):
            for row, value in enumerate(List):
                if value == 2:
                    dp.append((line, row))
                elif value == 1:
                    g_count += 1
        if g_count == 0:
            return 0
        
        while dp:
            lenth = len(dp)
            if g_count == 0:
                break
            for _ in range(lenth):
                x, y = dp.pop(0)
                # up
                if x != 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    g_count -= 1
                    dp.append([x-1,y])
                # down
                if x < len1-1 and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    g_count -= 1
                    dp.append([x+1,y])
                # left
                if y != 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    g_count -= 1
                    dp.append([x,y-1])
                # right
                if y < len2-1 and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    g_count -= 1
                    dp.append([x,y+1])
            ans += 1
            
        if g_count != 0:
            return -1
        return ans        
