from collections import defaultdict
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.ans = defaultdict(int)
        self.t2 = defaultdict(int)
        for i in dictionary:
            lenth = len(i)
            if lenth > 2:
                self.ans[i[0]+str(lenth-2)+i[-1]] += 1
            self.t2[i] += 1
            
    def isUnique(self, word: str) -> bool:
        t = 1 if word not in self.t2 else 2
        lenth = len(word)-2
        if len(word) <= 2:
            return True if self.t2[word] < t+1 else False
        return True if self.ans[word[0]+str(lenth)+word[-1]] < t else False

