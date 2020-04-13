class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        row = [0 for i in range(len(grid[0]))]
        for i in grid:
            s = sum(i)
            if s > 1:
                ans += s
                for index, value in enumerate(i):
                    if row[index] == 1 and value != 0:
                        ans += 1
                    if value != 0:
                        row[index] += s
            else:
                for index, value in enumerate(i):
                    if value == 1:
                        if row[index] == 1:
                            ans += 2
                        elif row[index] > 1:
                            ans += 1
                        row[index] += 1
                        break
        return ans
