class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def check(r=root):
            if not r:
                return False
            left =  check(r.left)
            right = check(r.right)
            if not left:
                r.left = None
            if not right:
                r.right = None
            return r.val == 1 or left or right
            
        return root if check() else None
