# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ans = ListNode(0)
        temp = ans.next
        nodelist = []
        while head:
            nodelist.append(head)
            head = head.next
            if len(nodelist) == 2:
                temp.next = nodelist[1]
                temp = temp.next
                temp.next = nodelist[1]
                temp = temp.next
                nodelist = []
        if nodelist:
            temp.next = nodelist[0]

        return ans.next
