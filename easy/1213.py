from collections import defaultdict

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        t = defaultdict(int)
        for i in arr1+arr2+arr3:
            t[i] += 1
        ans = []
        for k, v in t.items():
            if v == 3:
                ans.append(k)
        ans.sort()
        return ans
