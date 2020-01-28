# 从下往上计算深度
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dp(root) != -1

    def dp(self, root):
        if not root:
            return 0
        left = self.dp(root.left)
        if left == -1:
            return -1
        right = self.dp(root.right)
        if right == -1:
            return -1
        return max(left, right) +1 if abs(left - right) < 2 else -1
