class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def check(lines=s, tmp=[]):
            if not lines :
                ans.append(tmp)
                return ""
            lenth = len(lines)
            if lenth == 1:
                ans.append(tmp+[lines])
                return ""
            for i in range(1, lenth+1):
                t = lines[0: i]
                if t == t[::-1]:
                    check(lines[i:], tmp+[t])
        check()
        return ans
