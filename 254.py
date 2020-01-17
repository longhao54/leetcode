# 很慢的笨方法
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = []
        self.getnums(n) 
        if not self.nums:
            return ans
        def backtrace(t=[], now=1, stop = n, nums = self.nums):
            if now == stop:
                ans.append(t)
            for index, value in enumerate(nums):
                tmp = now*value
                if tmp <= stop:
                    backtrace(t+[value], tmp, stop, nums[index:])
        backtrace()
        return ans

    def getnums(self, n):
        self.nums = []
        start = 2
        while start < n//2+1:
            if n % start == 0:
                self.nums.append(start)
            start += 1

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def helper(temp,factor,n):
            while factor * factor <= n:
                if n % factor == 0:
                    result.append(temp + [factor,n // factor])
                    helper(temp + [factor],factor,n // factor)
                factor += 1
        result = []
        helper([],2,n)
        return result
