class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        n = []
        def check(node):
            if not node:
                return ""
            check(node.left)
            n.append(node.val)
            check(node.right)
            
        check(root)
        t = TreeNode(0)
        a = t
        for i in n:
            t.right = TreeNode(i)
            t = t.right
        return a.right

# 改进 遍历一次
t = TreeNode(0)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        a = t
        def check(node):
            global t
            if not node:
                return ""
            check(node.left)
            t.right = TreeNode(node.val)
            t = t.right
            check(node.right)
            
        check(root)
        return a.right
