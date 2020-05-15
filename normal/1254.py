class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def markAs3(grid_child: List[List[int]], i: int, j: int):
            grid_child[i][j] = 2
            if i > 0 and grid_child[i - 1][j] == 0:
                markAs3(grid_child, i - 1, j)
            if i < len(grid_child) - 1 and grid_child[i + 1][j] == 0:
                markAs3(grid_child, i + 1, j)
            if j > 0 and grid_child[i][j - 1] == 0:
                markAs3(grid_child, i, j - 1)
            if j < len(grid_child[0]) - 1 and grid_child[i][j + 1] == 0:
                markAs3(grid_child, i, j + 1)

        # mark non isolated lands
        row_all = len(grid)
        col_all = len(grid[0])
        for col in range(col_all):
            if grid[0][col] == 0:
                markAs3(grid, 0, col)
            if grid[row_all - 1][col] == 0:
                markAs3(grid, row_all - 1, col)
        for row in range(row_all):
            if grid[row][0] == 0:
                markAs3(grid, row, 0)
            if grid[row][col_all - 1] == 0:
                markAs3(grid, row, col_all - 1)
        # check all lands
        count = 0
        for y in range(row_all):
            for x in range(col_all):
                if grid[y][x] == 0:
                    markAs3(grid, y, x)
                    count += 1
        return count
