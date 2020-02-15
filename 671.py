class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        a1, a2 = float("inf"), float("inf")
        dp=[root]
        if not dp:
            return -1
        while dp:
            t = dp.pop()
            if t.val not in [a1, a2]:
                if t.val < a1:
                    a1 = t.val
                elif t.val < a2:
                    a2 = t.val
            if t.left:
                dp.append(t.left)
            if t.right:
                dp.append(t.right)
        if a1 == a2 or a1 == float("inf") or a2 == float('inf'):
            return -1
        return a2
