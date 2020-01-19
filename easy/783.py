class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.m = float('inf')
        self.nums = []
        def backtrace(node):
            self.nums.append(node.val)
            if node.left:
                backtrace(node.left)
            if node.right:
                backtrace(node.right)
        backtrace(root)
        self.nums.sort()
        start = self.nums[0]
        for i in self.nums[1:]:
            self.m = min(self.m, abs(i-start))
            if self.m == 1:
                return 1
            start = i
        return self.m

# 最快答案
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans
