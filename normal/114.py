class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """ 
        if not root:
            return None
        dp = [root]
        t = []
        while dp:
            a = dp.pop()
            t.append(a.val)
            if a.right:
                dp.append(a.right)
            if a.left:
                dp.append(a.left)
        if len(t) > 1:
            root.left = None
            t1 = root
            for i in t[1:]:
                t1.right = TreeNode(i)
                t1 = t1.right


# 最快答案
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        res = TreeNode(0)
        while stack:
            temp = stack.pop()
            res.right = temp
            res.left = None
            res = res.right
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        root = res.right
