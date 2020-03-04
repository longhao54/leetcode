class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        used = [start]
        dp = [start]
        len1 = len(maze)
        len2 = len(maze[0])
        def check(t1, t2):
            if [t1,t2] not in used:
                used.append([t1, t2])
                dp.append([t1, t2])
        while dp:
            for t in range(len(dp)):
                x, y = dp.pop(0)
                # left
                t1, t2 = x,y
                while t2 != 0 and maze[t1][t2-1] != 1:
                    t2 -= 1
                check(t1, t2)
                # right
                t1, t2 = x,y
                while t2 != len2-1 and maze[t1][t2+1] != 1:
                    t2 += 1   
                check(t1, t2)
                # up
                t1, t2 = x, y
                while t1 != 0 and maze[t1-1][t2] != 1:
                    t1 -= 1
                check(t1, t2)
                # down
                t1, t2 = x, y
                while t1 != len1-1 and maze[t1+1][t2] != 1:
                    t1 += 1
                check(t1, t2)
            if destination in used:
                return True
        return False
