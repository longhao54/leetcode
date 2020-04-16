class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.pos = [x for x in range(combinationLength)]
        self.finished = False

    def next(self) -> str:
        ans = "".join([self.s[p] for p in self.pos])
        i = -1
        for k in range(len(self.pos) - 1, -1, -1):
            if self.pos[k] != len(self.s) - len(self.pos) + k:
                i = k
                break
        if i == -1:
            self.finished = True
        else:
            self.pos[i] += 1
            for j in range(i + 1, len(self.pos)):
                self.pos[j] = self.pos[j - 1] + 1
        return ans

    def hasNext(self) -> bool:
        return not self.finished

