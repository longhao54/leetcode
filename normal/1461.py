class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        s_len = len(s)
        if s_len < 2 ** k:
            return False
        curr = set()
        for i in range(s_len+1-k):
            curr.add(s[i:k+i])
        if len(curr) >= 2 ** k:
            return True
        else:
            return False
