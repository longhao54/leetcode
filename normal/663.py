class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        ans = []
        
        def check(r):
            nonlocal s
            if not r:
                return 0
            left = check(r.left)
            right = check(r.right)
            s = r.val + left + right
            ans.append(s)
            return s
        s = check(root)
        ans.pop()
        return s / 2.0 in ans 
