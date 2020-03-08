class Solution:
    def minSwaps(self, data: List[int]) -> int:
        c = data.count(1)
        start = 0
        a = float("inf")
        m = c - data[start:start+c].count(1)
        a = min(m, a)
        while start < len(data) - c:
            if data[start] == 0:
                m -=1
            if data[start+c] == 0:
                m += 1
            start += 1
            a = min(m, a)
        return a
