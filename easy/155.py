class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ans = []

    def push(self, x: int) -> None:
        self.ans.append(x)

    def pop(self) -> None:
        self.ans.pop()

    def top(self) -> int:
        return self.ans[-1]

    def getMin(self) -> int:
        return min(self.ans)


# 最快答案
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.data=[]
        self.min=[]
        

    # 因为是先进先出 所以这么写确实没问题
    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.min)==0:
            self.min.append(x)
        elif self.min[-1]>=x:
            self.min.append(x)

    def pop(self) -> None:
        x=self.data[-1]
        self.data.pop(-1)
        if x==self.min[-1]:
            self.min.pop(-1)

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]

