class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        dp = [root]
        if not root:
            return []
        while dp:
            t = dp.pop()
            ans.append(t.val)
            if t.right:
                dp.append(t.right)
            if t.left:
                dp.append(t.left)
            
        return ans
