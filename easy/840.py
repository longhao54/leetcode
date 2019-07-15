class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        self.check = set([1,2,3,4,5,6,7,8,9])
        if len(grid) == 3 and len(grid[0]) ==3:
            if self.checknum(grid) :
                    count += 1
            return count
        # elif len(grid)== 3:
        #     for j in range(len(grid[0])-2):
        #         if self.checknum([grid[0][j:j+3], grid[1][j:j+3], grid[2][j:j+3]]) == check :
        #             count += 1
        #     return count
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if self.checknum([grid[i][j:j+3], grid[i+1][j:j+3], grid[i+2][j:j+3]]) :
                    count += 1
        return count


    def checknum(self, g):
        if len(set([sum(g[0]), sum(g[1]), sum(g[2]), sum([g[0][0], g[1][1], g[2][2]]), sum([g[0][2], g[1][1], g[2][0]]),
                    sum([g[0][0], g[1][0], g[2][0]]), sum([g[0][1], g[1][1], g[2][1]]), sum([g[0][2], g[1][2], g[2][2]]) ])) == 1 and set(g[0]+g[1]+g[2]) == self.check:
            return True
        return False

a = Solution()
print(a.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
print(a.numMagicSquaresInside([[2,7,6],[1,5,9],[4,3,8]]))
print(a.numMagicSquaresInside([[5,5,5],[5,5,5],[5,5,5]]))