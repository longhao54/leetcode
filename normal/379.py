class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.d = {}
        self.unused = set()
        for i in range(maxNumbers):
            self.d[i] = True
            self.unused.add(i)

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if not self.unused:
            return -1
        t1 = self.unused.pop()
        self.d[t1] = False
        return t1
        
        

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return self.d[number]
        

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.unused.add(number)
        self.d[number] = True
        


