class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        ans = Node(root.val)
        def check(dp1, dp2):
            for tmp in dp2:
                t = Node(tmp.val)
                check(t.children, tmp.children)
                dp1.append(t)
        check(ans.children, root.children)
        return ans
