from collections import defaultdict
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        fat = defaultdict(list)
        for f, s in zip(pid, ppid):
            fat[s].append(f)
        ans = set()
        def check(kill):
            if kill not in fat:
                return ""
            for i in fat[kill]:
                if i != 0 and i not in ans:
                    ans.add(i)
                    check(i)
        ans.add(kill)
        check(kill)
        return ans
