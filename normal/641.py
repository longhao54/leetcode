class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.ans = []
        self.max = k
        self.now = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.now < self.max:
            self.ans.insert(0, value)
            self.now += 1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.now < self.max:
            self.ans.append(value)
            self.now += 1
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.now:
            self.ans.pop(0)
            self.now -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.now:
            self.ans.pop()
            self.now -= 1
            return True
        return False
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.ans:
            return self.ans[0]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.ans:
            return self.ans[-1]
        return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.now == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.now == self.max
        
