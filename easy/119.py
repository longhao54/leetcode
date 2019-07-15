'''

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

'''


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        for i in range(rowIndex + 1):
            List = []
            for j in range(i):
                if j == 0 or j + 1 == i:
                    List.append(1)
                else:
                    List.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(List)

            # print(ans)
        return ans[rowIndex-1]