class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        newO = []
        for o in obstacles:
            if o[0] > x or o[1] > y:
                continue
            else:
                newO.append(o)

        xx = 0
        yy = 0
        for s in command:
            if s == "U":
                yy += 1
            else:
                xx += 1
        if self.reach(x,y,xx,yy,command):
            for o in newO:
                if self.reach(o[0],o[1],xx,yy,command):
                    return False
            return True
        else:
            return False

        
    def reach(self, x1,y1,xx,yy,command):
        start = int((x1+y1)/(xx+yy))
        point = [start*xx, start*yy]
        step = (x1+y1)%(xx+yy)
        if step != 0:
            for s in command[:step]:
                if s == "U":
                    point[1] += 1
                else:
                    point[0] += 1
        if x1 == point[0] and y1 == point[1]:
            return True
        else:
            return False
