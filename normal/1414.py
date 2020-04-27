class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a, b = 1, 1
        tmp = [1, 1]
        while a+b <= k:
            tmp.append(a+b)
            a, b = b, a+b
        ans = 0
        for i in tmp[::-1]:
            if i <= k:
                k -=i
                ans += 1
            if k == 0:
                break
        return ans
