class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root:
            if arr: return False
            return True
        def dfs(root, arr):
            if not arr: return False
            if root.val != arr[0]:
                return False
            if root.left:
                if dfs(root.left, arr[1:]):
                    return True
            if root.right:
                if dfs(root.right, arr[1:]):
                    return True
            if not root.left and not root.right:
                if not arr[1:]:
                    return True
                return False
        return dfs(root, arr)
