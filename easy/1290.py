class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a = ""
        ans = 0
        while head:
            a += str(head.val)
            head = head.next
        lenth = len(a) - 1
        for i in a:
            i = int(i)
            ans += 2**lenth * i
            lenth -= 1
        return ans
