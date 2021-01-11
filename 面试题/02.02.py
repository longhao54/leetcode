class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        a=head
        b=head
        for i in range(k):
            b=b.next
        while b:
            a=a.next
            b=b.next
        return a.val
