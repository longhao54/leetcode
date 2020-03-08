from collections import defaultdict
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(bool)
        self.c = defaultdict(bool)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = ""
        for i in word:
            t += i
            self.d[t] = True
        self.c[word] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.c[word]



    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.d[prefix]
