class StringIterator:

    def __init__(self, compressedString: str):
        lastn = False
        self.s = []
        self.nums = []
        last = ""
        n = 0
        for i in compressedString:
            if i not in "1234567890":
                self.s.append(i)
                self.nums.append(n)
                last = i
                n = 0
            else:
                n = n *10 + int(i)
        self.nums.pop(0)
        self.nums.append(n)
        
    def next(self) -> str:
        if self.s:
            t = self.s[0]
        else:
            return " "
        if self.nums[0] > 1:
            self.nums[0] -= 1
        else:
            self.nums.pop(0)
            self.s.pop(0)
        return t
        

    def hasNext(self) -> bool:
        return True if self.nums else False
