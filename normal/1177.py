class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        cnt = [0]
        for i, v in enumerate(s):
            cnt.append(cnt[i] ^ 1 << (ord(v) - 97))
        return (bin(cnt[j + 1] ^ cnt[i]).count('1') // 2 <= k for i, j, k in queries)
