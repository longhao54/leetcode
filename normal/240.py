class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l, r = len(matrix)-1, 0
        while l >= 0 and r < len(matrix[0]):
            t = matrix[l][r]
            if t == target:
                return True
            elif t > target:
                l -= 1
            else:
                r += 1
        return False
