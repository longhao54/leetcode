class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [ [1] * m ] + [ [1] + [0]*(m-1) for _ in range(n-1)]
        for i in range(1, n):
            for j in range(1, m):
                a[i][j] = a[i-1][j] + a[i][j-1]
        return a[-1][-1]


        # 横着看 上面的是 按列处理的  下面这个方法是 按行处理的
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]

