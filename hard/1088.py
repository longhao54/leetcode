class Solution:
    def confusingNumberII(self, N: int) -> int:
        ans = 0
        tmp = {"1":"1", "8":"8", "6":"9", "9":"6", "0":"0"}
        def check(n, lenth):
            nonlocal ans
            if n > N:
                return ""
            t = ""
            for i in str(n)[::-1]:
                t += tmp[i]
            if int(t) != n:
                ans += 1
            for i in (0,1,6,8,9):
                check(n*10+i, lenth+1)

        for i in (1,6,8,9):
            check(i, 1)
        return ans
