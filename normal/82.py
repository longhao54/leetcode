class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t = ListNode(0)
        a = t
        head = head
        last = ""
        other = []
        c = set()
        while head:
            if last == head.val:
                c.add(head.val)
            else:
                other.append(head.val)
            last = head.val
            head = head.next
        for i in c:
            other.remove(i)
        for i in other:
            t.next = ListNode(i)
            t = t.next
        return a.next
