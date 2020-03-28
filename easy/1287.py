class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        t = len(arr)//4
        if len(arr) < 4:
            return arr[0]
        for i, v in enumerate(arr):
            if arr[i] == arr[i+t]:
                return arr[i]
