class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans = False
        def check(a, b, s):
            nonlocal ans
            if a.startswith("0") and a != "0" or b.startswith("0") and b != "0" or not s:
                return ""
            while s: 
                t = str(int(a)+int(b))
                if s.startswith(t):
                    a, b = b, t
                    s = s.replace(t, "", 1)
                else:
                    return ""
            ans = True
        num = str(num)
        lenth = len(num)
        for i in range(lenth//2+1):
            for j in range(i+1, lenth):
                check(num[0:i+1], num[i+1:j+1], num[j+1:])
            
        return ans
