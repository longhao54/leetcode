from typing import List

class Solution:
    def dfs(self, depth, l):
        sum = 0
        for val in l:
            if val.isInteger():
                sum += val.getInteger() * depth
            else:
                sum += self.dfs(depth+1, val.getList())
        return sum

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.dfs(1, nestedList)
