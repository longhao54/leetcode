class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        lenth = 0
        list_d = {}
        if not head:
            return head
        while head:
            lenth += 1
            list_d[lenth] = head
            head = head.next
        mod = k % lenth
        if mod == 0:
            return list_d[1]
        target = lenth - mod
        list_d[target].next = None
        list_d[lenth].next = list_d[1]
        return list_d[target+1]



# 先整成环形链表 再切断  答案
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        start,end,len = head,None,0
        while head:
            end = head
            head = head.next
            len += 1
        end.next = start
        pos = len - k % len
        while pos > 1:
            start = start.next
            pos -= 1
        ret = start.next
        start.next = None
        return ret
