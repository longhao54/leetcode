class Solution:
    def checkValidString(self, s: str) -> bool:
        index_left, index_Any = [], []
        count = 0
        for i in s:
            if i == "(":
                index_left.append(count)
            elif i == ")":
                if index_left:
                    index_left.pop()
                elif index_Any:
                    index_Any.pop()
                else:
                    return False
            else:
                index_Any.append(count)
            count += 1
        
        lenth = index_left.__len__()
        if lenth <= index_Any.__len__():
                for i in index_left:
                    while index_Any and i > index_Any[0]:
                        index_Any.pop(0)
                    if index_Any:
                        index_Any.pop(0)
                        lenth -= 1
        return lenth <= index_Any.__len__()

    def fast(self, s):
        vset = set([0])
        for c in s:
            nset = set()
            if c == '*':
                for v in vset:
                    nset.add(v + 1)
                    nset.add(v)
                    if v >= 1: nset.add(v - 1)
            elif c == '(':
                for v in vset:
                    nset.add(v + 1)
            elif c == ')':
                for v in vset:
                    if v >= 1: nset.add(v - 1)
            vset = nset
        return 0 in vset
