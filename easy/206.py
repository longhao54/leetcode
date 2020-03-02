# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = []
        while head:
            temp.append(head.val)
            head = head.next

        if not temp:
            return None
        head = ListNode(temp[-1])
        Temp = head
        if len(temp) > 1:
            for i in temp[-2::-1]:
                Temp.next = ListNode(i)
                Temp = Temp.next

        # Temp.next = head
        return head

    def fast(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

# 较快的做法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            t = head.next
            head.next = last
            last = head
            if not t:
                break
            head = t
        return head
