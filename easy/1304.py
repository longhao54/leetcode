class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n % 2 == 1:
            ans.append(0)
            n -= 1
        start = 1
        while  n > 0:
            ans.append(start)
            ans.append(-start)
            n -= 2
            start += 1
        return ans
