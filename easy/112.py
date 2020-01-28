class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        st = [(root, sum)]

        while st:
            node, value = st.pop()
            value -= node.val
            if not node.left and not node.right and value == 0:
                return True
            if node.left:
                st.append((node.left, value))
            if node.right:
                st.append((node.right, value))

        return False
