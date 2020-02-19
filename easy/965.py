class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        v = root.val
        dp = [root]
        while dp:
            t = dp.pop()
            if t:
                if t.val != v:
                    return False
                dp.append(t.left)
                dp.append(t.right)
        return True
