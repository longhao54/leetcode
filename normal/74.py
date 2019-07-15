class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i and target <= i[-1]:
                return target in i 
        return False

    def fast(self, matrix: List[List[int]], target: int):
        rows = len(matrix)
        low = 0
        high = rows - 1
        exists = False
        while low <= high:
            mid = (low + high) // 2
            if not matrix[mid]:
                break
            if target < matrix[mid][0]:
                high = mid - 1
            else:
                if target <= matrix[mid][-1]:  # search in this row
                    low = 0
                    high = len(matrix[mid]) - 1
                    while low <= high:
                        m = (low + high) // 2
                        if target == matrix[mid][m]:
                            exists = True
                            break
                            
                        if target < matrix[mid][m]:
                            high = m - 1
                        else:
                            low = m + 1
                    break
                else:
                    low = mid + 1
        return exists
