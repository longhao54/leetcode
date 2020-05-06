class CustomStack:

    def __init__(self, maxSize: int):
        self.ans = []
        self.size = maxSize
        self.now = 0


    def push(self, x: int) -> None:
        if self.now < self.size:
            self.ans.append(x)
            self.now += 1


    def pop(self) -> int:
        if self.now != 0:
            self.now -= 1
            return self.ans.pop()
        return -1


    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.now)):
            self.ans[i] += val
