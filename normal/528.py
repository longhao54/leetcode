import random

class Solution:

    def __init__(self, w: List[int]):
        self.ans = {}
        self.last = 0
        self.lenth = len(w)
        for index, i in enumerate(w):
            self.ans[index] = self.last + i
            self.last += i
        
        
    def pickIndex(self) -> int:
        p = random.randint(1, self.last)
        if p <= self.ans[0]:
            return 0
        
        start = 0
        end = self.lenth-1
        while True:
            mid = (start + end) // 2
            t1, t2 = self.ans[mid], self.ans[mid+1]
            if p < t1:
                end = mid
                continue
            elif p == t1:
                return mid
            elif p > t1 and p <= t2:
                return mid+1
            else:
                start = mid
            
