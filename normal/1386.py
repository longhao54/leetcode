class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        t = [0]*10
        reservedSeats.sort()
        s = 0
        c = n
        def check(t):
            nonlocal n
            n -= 1
            if sum(t[1:9]) == 0:
                return 2
            elif sum(t[3:7]) == 0 or sum(t[1:5]) == 0 or sum(t[5:9]) == 0:
                return 1
            return 0
        ans = 0
        for i in reservedSeats:
            x, y = i
            if x != s:
                if s != 0:
                    ans += check(t)
                t = [0] * 10
                s = x
            t[y-1] = 1
        ans += check(t)
        if n != 0:
            ans += 2*n
        return ans
