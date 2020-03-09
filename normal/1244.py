class Leaderboard:
    def __init__(self):
        self.nameset = set()
        self.score = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.nameset:
            self.nameset.add(playerId)
            self.score.append([playerId, score])
        else:
            for i, c in enumerate(self.score):
                if c[0] == playerId:
                    c[1] += score
                    break
        self.score.sort(key = lambda x: x[1], reverse=True)

    def top(self, K: int) -> int:
        res = 0
        for i in range(K):
            res += self.score[i][1]
        return res

    def reset(self, playerId: int) -> None:
        for i, c in enumerate(self.score):
            if c[0] == playerId:
                self.score.pop(i)
        self.nameset.remove(playerId)
