class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        s = set()
        t1 = matrix[0]
        s.add(min(t1))
        for line in matrix[1:]:
            for i, v in enumerate(line):
                t1[i] = max(t1[i], v)
                s.add(min(line))
        return [ i for i in s if i in t1]
