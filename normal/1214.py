class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        d1 = {}
        dp1 = [root1]
        while dp1:
            t = dp1.pop()
            if t:
                d1[t.val] = 1
                dp1.append(t.left)
                dp1.append(t.right)
        dp2 = [root2]
        while dp2:
            t = dp2.pop()
            if t:
                T = target - t.val
                if d1.get(T,0):
                    return True
                dp2.append(t.left)
                dp2.append(t.right)
        return False
