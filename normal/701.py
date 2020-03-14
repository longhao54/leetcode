class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def check(r = root, v = val):
            if v > r.val:
                if r.right:
                    check(r.right, v)
                else:
                    r.right = TreeNode(v)
            else:
                if r.left:
                    check(r.left, v)
                else:
                    r.left = TreeNode(v)
        check(root, val)
        return root
