class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        lx, ly = len(A)-1, len(A[0])-1
        
        def check(x, y):
            nonlocal lx, ly
            if A[x][y] == 1:
                A[x][y] = 2
            else:
                return ""
            # up
            if x != 0:
                check(x-1, y)
            # down
            if x != lx:
                check(x+1, y)
            # left
            if y != 0:
                check(x, y-1)
            # right
            if y != ly:
                check(x, y+1)
        
        for x, line in enumerate(A):
            for y, v in enumerate(line):
                if v == 1 and x in [0, lx] or y in [0, ly]:
                    check(x, y)
        
        ans = 0
        
        for x, line in enumerate(A):
            for y, v in enumerate(line):
                if v == 1:
                    ans += 1
        return ans
