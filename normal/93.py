class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s) > 12:
            return []
        def backtrace(s1=s, t=[], pointc = 0):
            if pointc > 4:
                return ""
            if pointc == 4 and not s1:
                ans.append(".".join(t))
                return ""
            if not s1:
                return ""
            backtrace(s1[1:], t+[s1[0]], pointc+1)
            if t and int(t[-1] + s1[0]) <= 255 and t[-1] != "0":
                t[-1] += s1[0]
                backtrace(s1[1:], t, pointc)
        backtrace()
        return ans
