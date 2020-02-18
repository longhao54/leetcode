class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        dp = root
        if not dp:
            return None
        while dp:
            if dp.val == val:
                return dp
            if dp.val > val:
                dp = dp.left
            else:
                dp = dp.right
        return None
