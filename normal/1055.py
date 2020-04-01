class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t = source
        ans = 1
        for i in target:
            if i not in source:
                return -1
            if not t:
                t = source
                ans += 1
            if i not in t:
                ans += 1
                t = source
            index = t.index(i)
            t = t[index+1:]
        return ans
