# 弱智解法
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        lenth = len(S)
        def backtrace(s=S, t=""):
            if not s and len(t) == lenth:
                ans.append(t)
                return ""
            for index, value in enumerate(s):
                if value not in "1234567890":
                    backtrace(s[index+1:], t+value.upper())
                    backtrace(s[index+1:], t+value.lower())
                else:
                    backtrace(s[index+1:], t+value)
        backtrace()
        return ans


# 较快答案
class Solution:
    def letterCasePermutation(self, S):
        res = ['']
        for s in S:
            if s.isalpha():
                res = res * 2
                for i in range(len(res)):
                    if i < len(res) / 2:
                        res[i] = res[i] + s.lower()
                    else:
                        res[i] = res[i] + s.upper()
            else:
                for i in range(len(res)):
                    res[i] = res[i] + s
        return res
