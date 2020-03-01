# 比较慢

from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        t1 = defaultdict(int)
        ans = 0
        for i in chars:
            t1[i] += 1
        for w in words:
            t = defaultdict(int)
            c = True
            tmp = 0
            for j in w:
                t[j] += 1
            for k, v in t.items():
                if v > t1[k]:
                    c = False
                    break
                else:
                    tmp += v
            if c:
                ans += tmp
        return ans

# copy 字典居然比上面快很多
from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        t1 = defaultdict(int)
        ans = 0
        for i in chars:
            t1[i] += 1
        for w in words:
            tmp = t1.copy()
            c = True
            lenth = 0
            for i in w:
                tmp[i] -= 1
                if tmp[i] < 0:
                    c = False
                    break
                lenth += 1
            if c:
                ans += lenth
        return ans
