# 很慢的方法
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        start = 0
        while start < len(words):
            t = words[start]
            s = 0
            c = True
            while s < len(t):
                if t[s:] in words[0:start] + words[start+1:]:
                    c = False
                    words.remove(t[s:])
                s += 1
            if c:
                start += 1
        s = sum(len(i) for i in words)
        return s + len(words)

# trie
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

