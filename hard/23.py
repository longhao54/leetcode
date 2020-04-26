# 差点就超时的方法
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = ListNode(0)
        t = ans
        def check():
            nonlocal t
            tmp = {}
            if not lists:
                return ""
            for i, v in enumerate(lists):
                if not v:
                    continue
                tmp[v.val] = i
            if not tmp.keys():
                return ""
            m = min(tmp.keys())
            lists[tmp[m]] = lists[tmp[m]].next
            if not lists[tmp[m]]:
                lists.pop(tmp[m])
            t.next = ListNode(m)
            t = t.next
            check()
            
        check()
        return ans.next

# 稍微快了一丢丢
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = ListNode(0)
        t = ans
        def check():
            nonlocal t
            tmp = float("inf")
            sindex = None
            if not lists:
                return ""
            for index, v in enumerate(lists):
                if not v:
                    continue
                if v.val < tmp:
                    tmp = v.val
                    sindex = index
            if sindex is not None:
                t.next = ListNode(tmp)
                t = t.next
                if not lists[sindex].next:
                    lists.pop(sindex)
                else:
                    lists[sindex] = lists[sindex].next
            else:
                return ""
            check()
        check()
        return ans.next

# 这就很快了
from collections import defaultdict
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = ListNode(0)
        t = ans
        tmp = defaultdict(list)
        for i, v in enumerate(lists):
            if v:
                tmp[v.val].append(i)
        def check():
            nonlocal t
            if not tmp or not lists:
                return ""
            m = min(tmp.keys())
            t.next = ListNode(m)
            t = t.next
            target = tmp[m].pop(0)
            if not tmp[m]:
                tmp.pop(m)
            if lists[target].next:
                lists[target] = lists[target].next
                tmp[lists[target].val].append(target)
            check()
            
        check()
        return ans.next
