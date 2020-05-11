class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        stack = deque()
        cur = root
        nodes = []
        while len(stack) > 0 or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                nodes.append(cur)
                right = cur.right
                cur.left = None
                cur.right = None
                cur = right
        head = self.struct_bst(nodes, 0, len(nodes) - 1)
        return head

    def struct_bst(self, nodes, left, right):
        if left > right:
            return None
        if left == right:
            return nodes[left]
        mid = (left + right) // 2
        nodes[mid].left = self.struct_bst(nodes, left, mid - 1)
        nodes[mid].right = self.struct_bst(nodes, mid + 1, right)
        return nodes[mid]

