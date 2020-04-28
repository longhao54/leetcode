# 方法对 但是超时
from collections import defaultdict
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        dic = defaultdict(list)
        for i, v in enumerate(croakOfFrogs):
            dic[v].append(i)
        if len(dic) != 5:
            return -1
        for v in dic.values():
            if len(v) != len(dic["c"]):
                return -1
        ans = 1
        t = {0:-1}
        for i in range(len(dic["c"])):
            check = True
            c, r, o, a, k = dic["c"].pop(0), dic["r"].pop(0), dic["o"].pop(0), dic["a"].pop(0), dic["k"].pop(0)
            if min(c,r,o,a,k) != c or max(c,r,o,a,k) != k:
                return -1
            for v in range(ans):
                if c > t[v]:
                    t[v]=k
                    c = False
                    break
            if c:
                t[ans] = k
                ans += 1
        return ans 

# 答案
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c=r=o=a=k=0
        now=0
        res=0
        for i in croakOfFrogs:
            if i=='c':
                c+=1
                now+=1
                res=max(res,now)
            elif i=='r':
                r+=1
            elif i=='o':
                o+=1
            elif i=='a':
                a+=1
            elif i=='k':
                k+=1
                now-=1
            if not c>=r>=o>=a>=k:
                return -1
        return res if now==0 else -1
