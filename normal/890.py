class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        if not words or not pattern:
            return []
        ans = []
        t = {}
        for i,v in enumerate(pattern):
            t[i] = v 
        for i in words:
            tmp = {}
            tmp2 = {}
            c = True
            for index, v in enumerate(i):
                if v in tmp and tmp[v] != t[index] or t[index] in tmp2 and tmp2[t[index]] != v:
                    c = False
                    break
                else:
                    tmp[v] = t[index]
                    tmp2[t[index]] = v
            if c:
                ans.append(i)
        return ans 
