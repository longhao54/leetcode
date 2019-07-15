class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        if matrix == []:
            return ret
        ret.extend(matrix[0]) # 上侧
        new = [reversed(i) for i in matrix[1:]]
        if new == []:
            return ret
        r = self.spiralOrder([i for i in zip(*new)])
        ret.extend(r)
        return ret
