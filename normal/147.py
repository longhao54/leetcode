# 比较慢
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        t = ListNode(head.val)
        head = head.next
        while head:
            val = head.val
            tmp = ListNode(val)
            p = t
            if val < t.val:
                tmp.next = t
                t = tmp
                head = head.next
                continue  
            while t:
                if t.val <= val and t.next and t.next.val > val:
                    tmp.next = t.next
                    t.next = tmp
                    break
                if not t.next:
                    t.next = tmp
                    break
                t = t.next
            t = p
            head = head.next
        return t


# 快一些的
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        cur = head
        while cur:
            tmp = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre= dummy
            cur = tmp
        return dummy.next
