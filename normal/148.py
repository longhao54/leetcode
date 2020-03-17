class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        t = []
        while head:
            t.append(head.val)
            head = head.next
        t.sort()
        if not t:
            return None
        ans = ListNode(t.pop(0))
        t1 = ans
        while t:
            t1.next = ListNode(t.pop(0))
            t1 = t1.next
        return ans
