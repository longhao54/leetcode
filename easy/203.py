'''

删除链表中等于给定值 val 的所有节点。

'''

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """


        self.List= []
        self.check(head, val, self.List)
        return self.List

    def check(self, head, val, List):
        if head == None:
            return List
        if head.val != val:
            List.append(head.val)
        head = head.next
        self.check(head, val, List)

    def other_removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        now = head
        next = None
        if head.next:
            next = head.next
        while next:
            if next.val == val:
                if next.next:
                    now.next = next.next
                else:
                    now.next = None
                    break
                next = now.next
            else:
                now = now.next
                next = next.next
        if head.val == val:
            return head.next
        return head