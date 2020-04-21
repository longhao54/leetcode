class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        lx, ly = len(image), len(image[0])
        moved = []
        def check(x, y, v):
            nonlocal newColor, lx, ly
            if image[x][y] != v or [x,y] in moved:
                return ""
            image[x][y] = newColor
            moved.append([x,y])
            #up
            if x != 0:
                check(x-1, y, v)
            #down
            if x != lx-1:
                check(x+1, y, v)
            #left
            if y != 0:
                check(x, y-1, v)
            #right
            if y != ly -1:
                check(x, y+1, v)
        check(sr, sc, image[sr][sc])
        return image
