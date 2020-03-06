class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        s = sum([customers[i] for i, v in enumerate(grumpy) if v == 0])
        ans = 0
        for i in range(X):
            if grumpy[i] == 1:
                s += customers[i]
        ans = max(ans, s)
        for i in range(0, len(customers)-X):
            if grumpy[i] == 1:
                s -= customers[i]
            if grumpy[i+X] == 1:
                s += customers[i+X]
            ans = max(ans, s)
        return ans
