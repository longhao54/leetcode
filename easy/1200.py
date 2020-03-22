from collections import defaultdict
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        if len(arr) <= 1:
            return []
        t = defaultdict(list)
        m = float("inf")
        last = arr[0]
        for i in arr[1:]:
            m = min(m, i-last)
            t[i-last].append([last, i])
            last = i
        return t[m]
