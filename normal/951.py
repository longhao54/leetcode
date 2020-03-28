class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        dp = [(root1, root2)]
        while dp:
            r1, r2 = dp.pop()
            if not r1 and r2 or r1 and not r2:
                return False
            if r1 and r2:
                if r1.val != r2.val :
                    return False
                if r1.left and r2.left and r1.left.val == r2.left.val or not r1.left and not r2.left):
                    dp.append((r1.left, r2.left))
                    dp.append((r1.right, r2.right))
                else:
                    dp.append((r1.left, r2.right))
                    dp.append((r1.right, r2.left))
        return True
