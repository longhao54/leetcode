class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        if not root :
            return ans
        def dp(root, trace=""):
            if not root.left and not root.right:
                ans.append(trace)
                return ""
            if root.left:
                dp(root.left, trace + "->" + str(root.left.val))
            if root.right:
                dp(root.right, trace + "->" + str(root.right.val))
        dp(root, str(root.val))
        return ans
