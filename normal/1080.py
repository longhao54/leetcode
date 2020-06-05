class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def check(root, val = 0):
            nonlocal limit
            val += root.val
            print(root.val, val)
            left = check(root.left, val) if root.left else 0
            right = check(root.right, val) if root.right else 0
            print(root.val, val, left, right)
            if left == "DROP":
                root.left = None
            if right == "DROP":
                root.right = None
            if not root.left and not root.right:
                if val < limit:
                    return "DROP"
        check(root)
        return root
