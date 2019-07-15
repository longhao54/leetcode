'''
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def make_list(List):
    a = ListNode(0)
    b = a
    for num in List:
        b.next = ListNode(num)
        b = b.next
    b = a.next
    return b
#
# def make_list2(num):  # 这种对于 1000000000000000000000000000466 数据特别长的时候 会 出现值偏差
#     a = []
#     while True:
#         mo = num % 10
#         num = int(num/10)
#         print(mo)
#         a.append(mo)
#         if num <10 :
#             a.append(num)
#             break
#     return a

def make_list2(string):
    count = []
    lenth = len(string)
    for i in range(lenth):
        count.insert(0,int(string[i]))
    return count

print(make_list2(str(1000000000000000000000000000466)))


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         sum = []
#         check = False
#         while True:
#             num = l1.val + l2.val
#             num = num + 1 if check else num
#
#             if num <= 9:
#                 sum.append(num)
#                 check = False
#             else:
#                 check = True
#                 sum.append(num-10)
#
#             if not l1.next and not l2.next:
#                 if check:
#                     sum.append(1)
#                 break
#             if not l1.next:
#                 l1 = ListNode(0)
#             else:
#                 l1 = l1.next
#             if not l2.next:
#                 l2 = ListNode(0)
#             else:
#                 l2 = l2.next
#         return sum

def change(numlist):
    a = numlist
    sum = []
    Sum = 0
    while True:
        sum.append(a.val)
        a = a.next
        if not a:
            break
    sum.reverse()
    for i in sum:
        Sum = Sum * 10 + i
    return Sum

class Solution:  # 这种方式 速度还不如上面的...
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = change(l1)
        b = change(l2)
        S = a + b
        # print(a)
        # print(b)
        # print(S)
        if  S >=10 :
            sum = make_list2(S)
        else:
            sum = [S]




        return sum

l1 = make_list([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
l2 = make_list([5,6,4])


a = Solution()
# a.addTwoNumbers(l1,l2)
# print(a.addTwoNumbers(l1,l2))