from collections import defaultdict
class Solution:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
        if not picture:
            return []
        ans = 0
        line = [0] * len(picture)
        row = [0] * len(picture[0])
        t = defaultdict(int)
        for x, l in enumerate(picture):
            t["".join(l)] += 1
            for y, v in enumerate(l):
                if v == "B":
                    line[x] += 1
                    row[y] += 1
                    
        for x, l in enumerate(picture):
            if t["".join(l)] != N:
                continue
            for y, v in enumerate(l):
                if v == "B":
                    if line[x] == row[y] == N:
                        ans += 1
        return ans
