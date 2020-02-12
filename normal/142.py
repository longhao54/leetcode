class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        t = set()
        while head:
            if head.next in t:
                return  head.next
            t.add(head)
            head = head.next
        return None
