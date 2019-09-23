import math
class Solution:
    def numSquares(self, n: int) -> int:   #  解法是对的 但是超时了
        # ans = collections.defaultdict(int)
        # for i in range(1, n+1):
        #     temp = 1
        #     ans[i] = i
        #     index = 1
        #     while i - temp  >= 0:
        #         ans[i] = min(ans[i], ans[i-temp]+1)
        #         temp = index*index
        #         index += 1
        # return ans[n]


'''
上面我的思路和解法是对的 但是在leetcode上运行超时 时间复杂度太大了

下面的是抄的参考答案的根据数学知识进行的 
四平方定理： 任何一个正整数都可以表示成不超过四个整数的平方之和。 推论：满足四数平方和定理的数n（四个整数的情况），必定满足 n=4^a(8b+7)
'''
            
        while n % 4 == 0: 
            n /= 4 
        if n % 8 == 7: 
            return 4 
        a = 0 
        while a**2 <= n: 
            b = int((n - a**2)**0.5) 
            if a**2 + b**2 == n: 
                return (not not a) + (not not b) 
            a += 1 
        return 3
