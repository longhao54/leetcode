class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        p = target.val
        dp = [cloned]
        while dp:
            t = dp.pop()
            if t:
                if t.val == p:
                    return t
                dp.append(t.left)
                dp.append(t.right)
