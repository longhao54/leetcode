class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrace(s, lc, rc):
            if lc == n and rc == n:
                ans.append(s)
                return
            if lc < n:
                backtrace(s+"(", lc+1, rc)
            if lc > rc:
                backtrace(s+")", lc, rc+1)
            
        backtrace("(", 1, 0)
        return ans
