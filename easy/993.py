class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return 
        dp = []
        if root.left:
            dp.append([root.left, root.val])
        if root.right:
            dp.append([root.right, root.val])
        while dp:
            count = 0
            fat = ""
            for i in range(len(dp)):
                t, f = dp.pop(0)
                if t.val in [x, y] and f != fat:
                    count += 1
                    fat = f
                if t.left:
                    dp.append([t.left, t.val])
                if t.right:
                    dp.append([t.right, t.val])
            if count == 2:
                return True
        return False
