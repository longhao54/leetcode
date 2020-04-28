class Solution:
    def numberOfSteps (self, num: int) -> int:
        s = bin(num)[2:]
        res = len(s) + sum([int(i) for i in s]) - 1
        return res
