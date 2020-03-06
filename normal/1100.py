from collections import defaultdict
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K:
            return 0
        ans = 0
        left = 0
        check = defaultdict(int)
        for i in S[0:K]:
            check[i] += 1
        if max(check.values()) < 2:
            ans += 1
        while left < len(S)-K:            
            check[S[left]] -= 1
            check[S[left+K]] += 1
            left += 1
            if max(check.values()) < 2:
                ans += 1
        return ans
            
