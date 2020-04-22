from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda a:len(a))
        count = defaultdict(dict)
        ans = 0
        for w in words:
            l = len(w)
            count[l][w] = 1
            if l-1 in count:
                for i in range(l):
                    t = w[0:i]+w[i+1:]
                    if t in count[l-1]:
                        count[l][w] = max(count[l-1][t] +1, count[l][w])
            ans = max(ans, count[l][w])
        return ans
