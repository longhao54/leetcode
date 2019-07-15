from collections import defaultdict

class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        w = defaultdict(list)
        for index, value in enumerate(words):
            w[value].append(index) 
        w1, w2 = w[word1], w[word2]
        if word1 == word2:
            last = w1[0]
            ans = []
            for i in w1[1::]:
                ans.append(i-last)
                last = i
            return min(ans)
        s1, s2 = 0, 0
        ans = abs(w1[s1] - w2[s2])
        while s1 < w1.__len__() and s2 < w2.__len__():
            ans = min([ans, abs(w1[s1] - w2[s2])])
            if w1[s1] < w2[s2]:
                s1 += 1
            else:
                s2 += 1
            
        return ans

    def fast(self, words, word1, word2):
        if word1 != word2:
            p, q = -1, -1
            ans = len(words) - 1
            for idx, word in enumerate(words):
                if word == word1: p = idx
                if word == word2: q = idx
                if (p!=-1) and (q!=-1): ans = min(ans, abs(p-q))
            return ans
        else:
             p = -1
             ans = len(words) - 1
             for idx, word in enumerate(words):
                if word == word1:
                    if p != -1:
                        ans = min(ans, abs(p-idx))
                    p = idx
             return ans
