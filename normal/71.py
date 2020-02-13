class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = path.split("/")
        t = []
        for i in ans:
            if not i :
                continue
            if i == ".":
                continue
            elif i == "..":
                if t:
                    t.pop()
            else:
                t.append(i)
        return "/" + "/".join(t)
