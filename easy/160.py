# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
 
        tempA = set()    # 用列表会超出时间限制
        while headA:
            tempA.add(headA)
            headA = headA.next

        while headB:
            if headB in tempA:
                return headB
            headB = headB.next

        return None

    def copy(self, headA, headB):
        if not headA or not headB:
            return 
        p,q = headA,headB
        while p!=q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
