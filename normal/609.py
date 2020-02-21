from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        t = defaultdict(list)
        ans = []
        for f in paths:
            f = f.split()
            path, files = f[0], f[1:]
            for file in files:
                fname, text  = file.split("(")
                text = text.replace(")","")
                t[text].append(path+"/"+fname)
        for _, v in t.items():
            if len(v) >= 2:
                ans.append(v)
        return ans
