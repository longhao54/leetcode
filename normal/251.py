class Vector2D(object):
    def __init__(self, v):
        self.list = []
        for nums in v:
            for num in nums:
                self.list.append(num)
        #print(self.list)
        self.index = 0
    
    def next(self):
        self.index += 1
        #print (self.index)
        return self.list[self.index-1]
    
    def hasNext(self):
        return self.index != (len(self.list) )

