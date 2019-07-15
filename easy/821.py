class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ids = [i for i, j in enumerate(S) if j == C]
        return [min([abs(i-j) for j in ids]) for i in range(len(S))]
