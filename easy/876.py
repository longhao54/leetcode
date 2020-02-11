class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a = []
        while head:
            a.append(head)
            head = head.next
        m = len(a) // 2
        return a[m]
