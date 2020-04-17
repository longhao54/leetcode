from collections import defaultdict
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0
        t = [0] * 26
        for i in tiles:
            t[ord(i)-ord("A")] += 1
            
        def check(ws, s):
            nonlocal ans
            ans += 1
            if s != 0:
                for i, v in enumerate(ws):
                    if v != 0:
                        check(ws[0:i] + [ws[i]-1]+ws[i+1:], s-1)
        
        check(t, sum(t))
        return ans-1
