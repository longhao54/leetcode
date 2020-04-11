class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        re = []
        for x, y in zip(A, B):
            c = True
            if x == y:
                continue
            for i in re:
                if x in i or y in i:
                    i.add(x)
                    i.add(y)
                    c = False
                    break
            if c:
                t = set()
                t.add(x)
                t.add(y)
                re.append(t)
        ans = ""
        check = {}
        
        rec = []
        if re:
            rec = [re[0]]
        for i in re:
            c = True
            for j in i:
                for w in rec:
                    if j in w:
                        c = False
                        for tmp in i:
                            w.add(tmp)
                        break
            if c:
                rec.append(i) 


        for i in rec:
            for w in i:
                check[w] = min(i)

        for i in S:
            if i in check:
                ans += check[i]
            else:
                ans += i
        return ans
