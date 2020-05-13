class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        def check(root):
            if not root:
                return ""
            if root.left:
                check(root.left)
            if root.right:
                check(root.right)
            ans.append(root.val)
        check(root)
        return ans
