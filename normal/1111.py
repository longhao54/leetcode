class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = [0]*len(seq)
        for i in range(1, len(seq)):
            if seq[i] == seq[i-1]: # 前后分到不同组
                res[i] = 1 - res[i-1]
            else:
                res[i] = res[i-1] # 前后同组
        return res
