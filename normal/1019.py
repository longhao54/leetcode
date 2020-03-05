# 通过 但是很慢
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        t = []
        while head:
            t.append(head.val)
            head = head.next
        tmp = []
        ans = []
        for i in t[::-1]:
            c = True
            while tmp:
                if i >= tmp[-1]:
                    tmp.pop()
                else:
                    ans.insert(0, tmp[-1])
                    c = False
                    break
            tmp.append(i)
            if c:
                ans.insert(0,0)
        return ans


# 最快答案
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        index_map = {}
        node_stack = []
        ret = []
        cur = head
        index = 0
        while cur:
            # push into stack
            index_map[cur] = index
            ret.append(0)
            while node_stack and node_stack[-1].val < cur.val:
                node = node_stack.pop()
                ret[index_map[node]] = cur.val
            node_stack.append(cur)
            cur, index = cur.next, index + 1
        return ret
