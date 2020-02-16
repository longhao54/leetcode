class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans
        def insert(node):
            for i in node.children:
                insert(i)
            ans.append(node.val)
        insert(root)
        return ans
