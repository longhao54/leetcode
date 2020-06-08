class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.res = []
        def dfs(root):
            if not root:
                return
            if not root.left and root.right:
                self.res.append(root.right.val)
            if not root.right and root.left:
                self.res.append(root.left.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res
