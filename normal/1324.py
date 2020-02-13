class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        ans = []
        count = 0
        m = max([len(i) for i in s])
        dic = {}
        for i in s:
            dic[i] = len(i)
        while count < m :
            t = ""
            check = False
            for i in s:
                if count < dic[i]:
                    t+=i[count]
                else:
                    check = True
                    t+= " "
            if check:
                sp = t.split()[-1]
                t = t.split(sp)
                t = sp.join(t[0:-1]) + sp
            ans.append(t)
            count += 1
        return ans

# 最快答案
return [''.join(i).rstrip() for i in itertools.zip_longest(*s.split(), fillvalue=' ')]
