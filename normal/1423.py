class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints)
        lenth = len(cardPoints)
        if lenth == k:
            return s
        now = sum(cardPoints[0:lenth-k])
        n = now
        t = lenth-k
        for i in range(lenth-k, lenth):
            now -= cardPoints[i-t]
            now += cardPoints[i]
            n = min(n, now)
        return s -n
