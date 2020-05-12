class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        m = 2**31-1
        def check(a, b, s):
            nonlocal m
            if int(a) > m or int(b) > m:
                return []
            tmp = []
            if a.startswith("0") and a != "0" or b.startswith("0") and b != "0" or not s:
                return []
            while s: 
                t = str(int(a)+int(b))
                if int(t) > m:
                    return []
                if s.startswith(t):
                    tmp.append(a)
                    a, b = b, t
                    s = s.replace(t, "", 1)
                else:
                    return []
            tmp.append(a)
            tmp.append(b)
            return tmp
        num = S
        lenth = len(S)
        for i in range(lenth//2+1):
            for j in range(i+1, lenth):
                ans = check(num[0:i+1], num[i+1:j+1], num[j+1:])
                if ans:
                    return ans
        return []
