# 这个超时
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def change(n):
            tmp = float("inf")
            n = str(n)
            for i in range(len(n)):
                t = n[0:i] + n[i+1:]
                if not t:
                    return 0
                if t[0] == 0:
                    t = t[1:]
                tmp = min(tmp, int(t))
            return tmp

        while k != 0:
            num = change(num)
            k -= 1
            if num == 0:
                break
        return str(num)

# 比较慢
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def change(n, l):
            if l <= 1:
                return "",0
            # if n[1] == "0":
            #     return n[2:], l-2
            a = n[1:]
            b = n[0] + n[2:]
            c = n[0:2] + n[3:]
            d = n[0:3] + n[4:]
            e = n[0:4] + n[5:]
            return min([a, b, c, d, e]), l-1
            
        lenth = len(num)
        while k != 0:
            num, lenth = change(num, lenth)
            k -= 1
            if not num:
                return "0"
            if num[0] == "0":
                num = num[1:]
                lenth -= 1
        
        return str(num) if num else "0"


# 最快答案
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result=[]
        for  c in num:
            while k  and result and result[-1]>c:
                result.pop()
                k-=1
            result.append(c)
        while k:
            result.pop()
            k-=1
        return "".join(result).lstrip("0") or "0"
