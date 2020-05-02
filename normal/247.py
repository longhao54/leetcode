class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        nums = {0:0, 1:1, 6:9, 8:8, 9:6}
        ns = (0,1,6,8,9)
        ans = []
        def check(t="", l = 0):
            nonlocal n
            if l == n:
                ans.append(t)
                return ""
            for i in ns:
                if i == 0 and n -l <= 2:
                    continue
                check(str(i)+t+str(nums[i]), l +2)
        
        if n % 2 == 0:
            check("", 0)
        else:
            check("0", 1)
            check("1", 1)
            check("8", 1)
        return ans
