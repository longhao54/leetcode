class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        cnt, ans = 0, 0
        for num, occ in freq.most_common():
            cnt += occ
            ans += 1
            if cnt * 2 >= len(arr):
                break
        return ans

