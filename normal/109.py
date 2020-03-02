class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        ans = []  
        while head:
            ans.append(head.val)
            head = head.next
        def check(left=0, right=len(ans)-1):
            if left > right:
                return None
            mid = (left+right) // 2
            root = TreeNode(ans[mid])
            root.left = check(left, mid-1)
            root.right = check(mid+1, right)
            return root
        return check()
