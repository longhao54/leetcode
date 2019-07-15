class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for __ in range(n)] for _ in range(n)]
        up,down,left,right = 0,n,0,n  #上下左右边界
        index = 1
        while  index <= n**2:
            for i in range(left,right):  #向右
                res[up][i] = index
                index += 1
            up += 1

            for i in range(up,down):     #向下
                res[i][right-1] = index
                index += 1
            right -= 1

            for i in range(right-1,left-1,-1):  #向左
                res[down-1][i] = index
                index += 1
            down -= 1

            for i in range(down-1,up-1,-1):  #向上
                res[i][left] = index
                index += 1
            left += 1

        return res
