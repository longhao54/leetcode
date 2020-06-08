class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return 0
        def check(root, value):
            nonlocal ans
            if root.val >= value:
                ans += 1
            if root.left:
                check(root.left, max(root.val, value))
            if root.right:
                check(root.right, max(root.val, value))

        check(root, float("-inf"))
        return ans
