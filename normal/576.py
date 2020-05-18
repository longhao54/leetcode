# 答案
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        MOD = 10 ** 9 + 7
        memo = collections.defaultdict(int)
        def dfs(memo, i, j, k):
            if (i, j, k) not in memo:
                if i < 0 or i >= m or j < 0 or j >= n:
                    memo[(i, j, k)] = 1
                elif k > 0:
                    for x, y in [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]:
                        memo[(i, j, k)] += dfs(memo, x, y, k - 1)
            return memo[(i, j, k)] 
        dfs(memo, i, j, N)
        return memo[(i, j, N)] % MOD

# 我做的 到76/94  超时
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        ans = 0
        mx, my = m-1, n-1
        def check(x, y, n):
            nonlocal ans, mx, my
            if n == 0:
                return ""
            # up
            if x != 0:
                check(x-1, y, n-1)
            else:
                ans += 1
            # down
            if x != mx:
                check(x+1, y, n-1)
            else:
                ans += 1
            # left
            if y != 0:
                check(x, y-1, n-1)
            else:
                ans += 1
            # right
            if y != my:
                check(x, y+1, n-1)
            else:
                ans += 1
        
        check(i, j, N)
        return ans % 1000000007

