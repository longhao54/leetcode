class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        nums = {0:0, 1:1, 6:9, 8:8, 9:6}
        ns = (0,1,6,8,9)
        ans = set()
        n1 = len(low)
        n2 = len(high)

        def check(t="", l = 0, n=0):
            if l == n and t:
                ans.add(t)
                return ""
            for i in ns:
                if i == 0 and n -l <= 2:
                    continue
                check(str(i)+t+str(nums[i]), l +2, n)
        
        for n in range(n1, n2+1):
            if n % 2 == 0:
                check("", 0, n)
            else:
                check("0", 1, n)
                check("1", 1, n)
                check("8", 1, n)
        t = 0
        for i in ans:
            if int(low) <= int(i) <= int(high):
                t+= 1
        return t
