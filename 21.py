'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''
def make_list(List):
    Node = []
    while True:
        if List.next:
            Node.append(List.val)
            List = List.next
        else:
            Node.append(List.val)
            break

    return Node


'''
20% 速度很慢

应该是在一次循环中 比较l1, l2的值 小的值添加到list中 并且小的链表进行 next
'''
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        Node = []
        Node += make_list(l1) if l1 else []
        Node += make_list(l2) if l2 else []
        Node.sort()
        return Node


