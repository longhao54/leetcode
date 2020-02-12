class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        count = 0
        temp = {}
        t = head
        while head:
            count += 1
            temp[count] = head
            head = head.next

        while count > 0:
            if temp[count].val < 9:
                temp[count].val += 1
                break
            else:
                temp[count].val = 0
                count -= 1
        if count == 0:
            t1 = ListNode(1)
            t1.next = t
            return t1
        return t
