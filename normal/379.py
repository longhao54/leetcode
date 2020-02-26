class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.d = {}
        print(maxNumbers)
        for i in range(maxNumbers):
            self.d[i] = True

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        for k, v in self.d.items():
            if v :
                self.d[k] = False
                return k
        return -1
        
        

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return self.d[number]
        

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.d[number] = True
        


