'''

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        '''
        
        if head == None:
            return head
        prev = head
        cur = head.next
        while cur:
            if cur.val != prev.val:
                prev.next = cur
                prev = cur
            else:
                prev.next = None
            cur = cur.next
        return head
        
        '''

        if not head:
            return []
        answer = set()
        while True:
            var = head.val
            head = head.next
            if var not in answer:
                answer.add(var)
            if head:
                continue
            else:
                break
        answer = list(answer)
        answer.sort()
        return answer