class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        rec = []
        for i in arr:
            c = set()
            check = True
            for t in i:
                if t in c:
                    check = False
                    break
                c.add(t)
            if check:
                rec.append(i)
                
        def check(s, ws):
            nonlocal ans
            ans = max(ans, len(s))
            if not ws:
                return ""
            for i, v in enumerate(ws):
                c = True
                for j in v:
                    if j in s:
                        c = False
                        break
                if c:
                    check(s+v, ws[i+1:])
        
        check("", rec)
        return ans
