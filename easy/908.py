class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        Max = max(A)
        Min = min(A)
        if Max-K > Min+K:
            return Max-Min-2*K
        else:
            return 0
