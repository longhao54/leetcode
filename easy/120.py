class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        lenth = triangle.__len__()
        if lenth == 2:
            return triangle[0][0] + min(triangle[1])
        elif lenth == 1:
            return triangle[0][0]
        elif lenth == 0:
            return 0
        triangle[1] = [ triangle[0][0] + i for i in triangle[1] ]
        
        for i in range(2, lenth):
            for index, _ in enumerate(triangle[i]):
                if index == 0:
                    triangle[i][index] += triangle[i-1][0]
                elif index == i:
                    triangle[i][index] += triangle[i-1][-1]
                else:
                    triangle[i][index] += min(triangle[i-1][index-1], triangle[i-1][index])
        
        return min(triangle[-1])
