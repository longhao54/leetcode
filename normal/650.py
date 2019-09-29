class Solution:
    '''
        这里想更快一点的话 其实 先求 n的所有整除的数 然后再计算 计算量会少很多
    '''
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        ans = [0, 0] + [ i  for i in range(2, n+1)]  
        for i in range(2,n+1):
            for j in range(2, i//2+1):
                if i %j == 0:
                    ans[i] = min(ans[i], ans[j] + i//j)
        return ans[-1]
            
