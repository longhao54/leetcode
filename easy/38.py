class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        if n==1: return num
        for i in range(2,n+1):
            p = []
            s = ""
            for x in num:
                if p==[] or x==p[0]:
                    p.append(x)
                else:
                    s += str(len(p))
                    s += p[0]
                    p = []
                    p.append(x)
            s += str(len(p))
            s += p[0]
            num = s
        return s
