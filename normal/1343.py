class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        if len(arr) < k:
            return 0
        index = k
        last = arr[0]
        s = sum(arr[0:k])
        if s/k >= threshold:
            ans += 1
        while index < len(arr):
            s += arr[index] - arr[index-k]
            index += 1
            if s/k >= threshold:
                ans += 1
        return ans
            
