class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        ans = [[0]*len(colsum) for i in range(2)]
        sc = sum(colsum)
        if sc != upper + lower or colsum.count(2) > upper:
            return []
        for i, v in enumerate(colsum):
            if v == 2:
                colsum[i] -= 1
                upper -= 1
                ans[0][i] = 1
                sc -= 1
            if upper == 0:
                break
        if upper > 0:
            for i, v in enumerate(colsum):
                if v != 0 and ans[0][i] != 1:
                    colsum[i] -= 1
                    upper -= 1
                    ans[0][i] = 1
                    sc -= 1
                if upper == 0:
                    break
        for i, v in enumerate(colsum):
            if v != 0 :
                colsum[i] -= 1
                ans[1][i] = 1
                lower -= 1
                sc -= 1
            if lower == 0:
                break
        if sc != 0 or upper != 0 or lower != 0:
            return []
        return ans
