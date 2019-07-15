class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        a = []
        for i in A:
            if i in a:
                return i
            a.append(i)
