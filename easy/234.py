# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        if ans:
            return ans == ans[::-1]
        return True
        

    def needstudy(self, head):
        fast = slow = head
        #  找到中点
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow: # 反转链表，可参考leetcode206
            slow.next, node, slow = node, slow, slow.next
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
