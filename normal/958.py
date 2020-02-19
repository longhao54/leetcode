class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return true
        dp = [root]
        last = True
        while dp:
            for i in range(len(dp)):
                t = dp.pop(0)
                if t.left:
                    dp.append(t.left)
                    if not last:
                        return False
                else:
                    last = False
                if t.right:
                    if not last:
                        return False
                    dp.append(t.right)
                else:
                    last = False
        return True
