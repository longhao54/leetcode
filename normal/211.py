# 一种硬算的方法  正常来说应该是要用 字典树来做的

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}


    def addWord(self, word: str) -> None:
        t = len(word)
        if len(word) in self.d:
            self.d[t] += [word]
        else:
            self.d[t] = [word]
    
    def search(self, word: str) -> bool:
        l_word = len(word)
        try:
            for i in self.d[l_word]:
                count = 0
                for ii in range(l_word):
                    if i[ii] == word[ii] or word[ii] == '.':
                        count +=1
                    else:
                        break
                if count == l_word:
                    return True
        except:
            return False
        return False

