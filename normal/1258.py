#弱智写法 后面的回溯步骤应该是和784的最快答案解法是一样的 

from collections import defaultdict
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        ans = []

        strings = defaultdict(list)
        final = defaultdict(list)
        lenth = len(text.split())
        for k, v in synonyms:
            strings[k].append(v)
            strings[v].append(k)
        
        for k, v in strings.items():
            final[k] += v
            for wr in v:
                for wrd in strings[wr]:
                    if wrd != k:
                        final[k].append(wrd)

        def backtrace(lines=[], s=text.split()):
            if not s and len(lines) == lenth:
                ans.append(" ".join(lines))
                return ""
            for index, value in enumerate(s):
                if value in final:
                    for v in final[value]:
                        backtrace(lines+[v], s[index+1:])
                backtrace(lines+[value], s[index+1:])

        backtrace()
        ans.sort()
        return ans
        

# 最快答案解法
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        w = set(itertools.chain(*synonyms))
        d = collections.defaultdict(set)
        p = {}
        rank = collections.defaultdict(int)
        for k in w:
            p[k] = k
            rank[k] = 1
            d[k] = {k}

        def get_root(x):
            while p[p[x]] != p[x]:
                p[x] = get_root(p[x])
            return p[x]

        def union(x, y):
            x_root = get_root(x)
            y_root = get_root(y)
            if rank[x_root] == rank[y_root]:
                p[y] = x_root
                rank[x_root] += 1
                d[x_root].update(d[y])
            elif rank[x_root] > rank[y_root]:
                p[y] = x_root
                d[x_root].update(d[y])
            else:
                p[x] = y_root
                d[y_root].update(d[x])

        for i, j in synonyms:
            union(i, j)
        for i, j in synonyms:
            union(i, j)

        words = text.split()
        n = len(words)

        def f(idx):
            if idx >= n:
                return [[]]
            if words[idx] in d:
                t = get_root(words[idx])
                return [[p] + s for p in d[t] for s in f(idx + 1)]
            return [[words[idx]] + s for s in f(idx + 1)]

        return sorted(map(" ".join, f(0)))

