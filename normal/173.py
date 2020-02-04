class BSTIterator:

    def __init__(self, root: TreeNode):
        self.start = 0
        self.ans = []
        dp = [root]
        while dp:
            for i in range(len(dp)):
                t = dp.pop(0)
                if t:
                    self.ans.append(t.val)
                    dp.append(t.left)
                    dp.append(t.right)
        self.ans.sort()
        self.lenth = len(self.ans)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        ans = self.ans[self.start]
        self.start += 1
        return ans

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.start != self.lenth
