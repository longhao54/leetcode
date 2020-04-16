class Solution:
    def expand(self, S: str) -> List[str]:
        l = []
        c = False
        for i in S:
            if i == ",":
                continue
            if i == "{":
                c = True
                l.append([])
                continue
            elif i == "}":
                c = False
                continue
            if c:
                l[-1].append(i)
            else:
                l.append([i])
        ans = []
        def check(s, strings = ""):
            if not s:
                ans.append(strings)
                return ""
            if len(s[0]) == 1:
                check(s[1:], strings+s[0][0])
            else:
                for i in range(len(s[0])):
                    check(s[1:], strings+s[0][i])
        
        check(l)
        return sorted(ans)
