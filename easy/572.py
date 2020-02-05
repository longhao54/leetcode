class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        dp = [s]
        while dp:
            for i in range(len(dp)):
                tmp = dp.pop(0)
                if tmp.val == t.val:
                    if self.check(tmp, t):
                        return True
                if tmp.left:
                    dp.append(tmp.left)
                if tmp.right:
                    dp.append(tmp.right)
        return False

    def check(self, root, r2):
        dp = [(root, r2)]
        while dp:
            t1, t2 = dp.pop()
            if not t1 and not t2:
                continue
            if t1 and not t2:
                return False
            if t2 and not t1:
                return False
            if t1.val != t2.val:
                return False
            dp.append((t1.left, t2.left))

