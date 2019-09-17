class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = obstacleGrid.__len__()
        n = obstacleGrid[0].__len__()

        check = False   # 为了判断第一行第一个数字是否为1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                if i == 0:
                    check = True
                obstacleGrid[0][i] = 0
                for j in range(i,n):
                    obstacleGrid[0][j] = 0
                break
            else:
                obstacleGrid[0][i] =1
        for i in range(1, m):     
            if check or obstacleGrid[i][0] == 1:
                for j in range(i,m):
                    obstacleGrid[j][0] = 0
                break
            else:
                obstacleGrid[i][0] = 1 
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        
        return obstacleGrid[-1][-1]
