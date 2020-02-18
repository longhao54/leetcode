class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def check(t):
            if not t:
                return ""
            check(t.left)
            ans.append(t.val)
            check(t.right)
        check(root)
        return ans
