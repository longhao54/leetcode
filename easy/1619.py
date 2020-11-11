class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr_len = len(arr)
        arr.sort()
        num = arr_len // 20
        avg = sum(arr[num:arr_len - num])
        return avg / float(arr_len - 2 * num)
