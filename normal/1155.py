class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dic = {i:1 for i in range(1, f+1)}
        for i in range(d-1):
            p = {}
            for key, v in dic.items():
                if key + f * (d-i) < target:
                    continue
                for k in range(1,f+1):
                    if k+key not in p:
                        p[k+key] = v
                    else:
                        p[k+key] += v
            dic = p 
        return dic[target]%1000000007 if target in dic else 0
