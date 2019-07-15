'''
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        List = []
        while True:
            if not head.next:
                List.append(head.val)
                break
            List.append(head.val)
            head = head.next
        List.reverse()
        List.pop(n - 1)
        List.reverse()
        return List