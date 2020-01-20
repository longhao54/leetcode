# for循环这块实在看不出来哪里错了

class Solution:
    def smallestFactorization(self, a: int) -> int:
        self.nums = []
        if a <= 3:
            return 0
        start = 2
        while start <= a:
            if start >= 10:
                return 0
            if a % start == 0:
                a /= start
                self.nums.append(start)
            else:
                start += 1
        if len(self.nums) <= 1:
            return 0
          
        ans = float("inf")    
        def backtrace(nums=self.nums[1:], t=[self.nums[0]]):
            if not nums:
                # print(t)
                t.sort()
            
            for index, value in enumerate(nums):
                if t == [2,8]:
                    print(nums)
                backtrace(nums[index+1:], t+[value])
                if t[-1]*value <= 9:
                    t[-1] *= value
                    backtrace(nums[index+1:], t)
                
                    
        backtrace()
        return ans

#  这个答案超时
class Solution:
    def smallestFactorization(self, a: int) -> int:
        self.nums = []
        if a in [1,2,3,5,7]:
            return a
        start = 2
        while start <= a:
            if start >= 10:
                return 0
            if a % start == 0:
                a /= start
                self.nums.append(start)
            else:
                start += 1
        if len(self.nums) <= 1:
            return 0
          
        self.ans = float("inf")    
        def backtrace(t=[self.nums[0]], start = 1):
            if start == len(self.nums):
                t.sort()
                a = 0
                for i in t:
                    a = a*10 + i
                self.ans = min(self.ans, a)
                
                return ""
            value = self.nums[start]
            backtrace(t+[value], start+1)
            if t[-1]*value <= 9:
                t[-1] *= value
                backtrace(t, start +1)
                
                    
        backtrace()
        return self.ans if self.ans <=  2147483647 else 0


# 正确答案 抄的
class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a==1:
            return 1
        stack = []
        for i in range(9,1,-1):
            while a % i == 0:
                a = a // i
                stack.append(i)
        if a != 1:
            return 0
        else:
            ans = 0
            while stack:
                ans = 10 * ans
                ans += stack.pop()
            return ans if ans < 2**31 -1 else 0

