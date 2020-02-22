class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        left, right = ListNode(0), ListNode(0)
        l, r = left, right
        c = 1
        while head:
            if c % 2 == 0:
                right.next = ListNode(head.val)
                right = right.next
            else:
                left.next = ListNode(head.val)
                left = left.next
            head = head.next
            c += 1
        if l.next:
            left.next = r.next
            return l.next
        else:
            return r.next


# 答案
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next.next == None:
            return head
        
        p = head.next  # 偶数位
        q = head.next.next  # 奇数位
        head.next = q
        t = p  # 记录第一个偶数位
        while q.next:
            p.next = p.next.next
            p = p.next
            q.next = q.next.next
            if q.next:  # 下一个奇数非空，才能进行赋值操作
                q = q.next
        q.next = t  # 连上第一个偶数位
        p.next = None  # 偶数位最后一个连上None
        return head
