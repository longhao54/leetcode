class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        t = sorted(set(arr))
        d = {v:i+1 for i, v in enumerate(t) }
        for i, v in enumerate(arr):
            arr[i] = d[v]
        return arr
