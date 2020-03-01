from collections import defaultdict

class FindElements:

    def __init__(self, root: TreeNode):
        self.ans = defaultdict(bool)
        dp = [(root, 0)]
        while dp:
            t, v = dp.pop()
            if t:
                self.ans[v] = True
                dp.append((t.left, v*2+1))
                dp.append((t.right, v*2+2))

    def find(self, target: int) -> bool:
        return self.ans[target]
