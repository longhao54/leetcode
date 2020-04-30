from collections import defaultdict
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tab = set()
        tmp = defaultdict(dict)
        menu = set()
        for i in orders:
            _, t, m = i
            menu.add(m)
            tab.add(int(t))
            if m in tmp[t]:
                tmp[t][m] += 1
            else:
                tmp[t][m] = 1
        
        tab = sorted(list(tab))
        menu = sorted(list(menu))
        ans = [["Table"] + menu]
        for i in tab:
            i = str(i)
            t = [i]
            for m in menu:
                if m in tmp[i]:
                    t.append(str(tmp[i][m]))
                else:
                    t.append(str(0))
            ans.append(t)
        return ans
