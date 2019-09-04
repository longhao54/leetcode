class LianBiao():
    def __init__(self, value, prev=None, Next=None):
        self.Next = Next
        self.prev = prev
        self.value = value

class MyLinkedList:

    def __init__(self):
        self.lenth = 0
        self.List = LianBiao(None)
        self.Head = self.List

    def get(self, index: int) -> int:
        print(index, self.lenth)
        if index+1 > self.lenth or index < 0:
            
            return -1
        temp = self.Head
        for i in range(index):
            temp = temp.Next
        return temp.value
            
    def addAtHead(self, val):
        self.lenth += 1
        self.Head.prev = LianBiao(val, Next = self.Head)
        self.Head = self.Head.prev

    def addAtTail(self, val: int) -> None:
        self.lenth += 1
        self.List.value = val
        self.List.Next = LianBiao(None, self.List)
        self.List = self.List.Next

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.lenth:
            self.addAtTail(val)
        elif index <= 0:
            self.addAtHead(val)
        elif index  < self.lenth:
            temp = self.Head
            for i in range(index - 1):
                temp = temp.Next
            New = LianBiao(val)
            after_temp = temp.Next
            New.prev, New.Next = temp, after_temp
            temp.Next, after_temp.prev = New, New
            self.lenth += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.Head = self.Head.Next
            self.lenth -= 1
        
        elif index < self.lenth and index > 0:
            temp = self.Head
            for i in range(index):
                temp = temp.Next
            before, after = temp.prev, temp.Next
            before.Next, after.prev = after, before
            self.lenth -= 1
            
        elif index +1 == self.lenth:
            Last = self.List.prev
            Last.Next = LianBiao(None)
            self.List = Last.Next
            self.lenth -= 1
        
