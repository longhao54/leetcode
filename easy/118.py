'''

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

'''

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ans = []
        for i in range(numRows+1):
            List = []
            for j in range(i):
                if j == 0 or j+1 ==i:
                    List.append(1)
                else:
                    List.append(ans[i-1][j-1]+ans[i-1][j])
            ans.append(List)
            # print(ans)
        return ans[1:]

a = Solution()
print(a.generate(5))