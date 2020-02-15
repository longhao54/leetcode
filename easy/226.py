class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        dp = [root]
        while dp:
            t = dp.pop()
            t.left, t.right = t.right, t.left
            if t.left:
                dp.append(t.left)
            if t.right:
                dp.append(t.right)
        return root
