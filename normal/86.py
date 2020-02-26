class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left, right = ListNode(0), ListNode(0)
        l, r = left, right
        while head:
            if head.val >= x:
                right.next = ListNode(head.val)
                right = right.next
            elif head.val < x:
                left.next = ListNode(head.val)
                left = left.next
            head = head.next
        left.next = r.next
        return l.next
