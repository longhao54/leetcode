# 这个方法超时了
from collections import defaultdict
class MyCalendarTwo:
    def __init__(self):
        self.d = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        for i in range(start, end):
            if self.d[i] == 2:
                for j in range(start, i):
                    self.d[j] -= 1
                return False
            else:
                self.d[i] += 1
        return True


# 答案
# 用两个区间标记 第一次重复的放到 overlaps里面
class MyCalendarTwo:
    def __init__(self):
        self.calendar = [] #单区
        self.overlaps = [] #双区

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True


