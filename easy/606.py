class Solution:
    def tree2str(self, t: TreeNode) -> str:
        ans = ""
        def check(root):
            nonlocal ans
            if not root:
                return ""
            ans += str(root.val)
            if root.left:
                ans += "("
                check(root.left)
                ans += ")"
            if not root.left and root.right:
                ans += "()("
                check(root.right)
                ans += ")"
            elif root.right:
                ans += "("
                check(root.right)
                ans += ")"
    
        check(t)
        return ans
