class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ans = ListNode(0)
        a = ans
        while head and head.next:
            t1 = head
            t2 = head.next
            head = t2.next
            ans.next = ListNode(t2.val)
            ans = ans.next
            ans.next = ListNode(t1.val)
            ans = ans.next
        if head:
            ans.next = ListNode(head.val)
            ans = ans.next
        return a.next


# 官方答案
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root_node = ListNode(-1)
        root_node.next = head

        prev_node = root_node

        while head and head.next:
            first_node = head
            second_node = head.next

            # 交换的过程
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            
            prev_node  = first_node
            head = first_node.next

        return root_node.next

