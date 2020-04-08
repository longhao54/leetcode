from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        c = 0
        tmp = defaultdict(int)
        for i in nums:
            if i %2 == 0:
                tmp[c]  += 1
            else:
                c += 1
                tmp[c] += 1
        for i in range(k+1, max(tmp)+1):
            ans += (tmp[i-k]) * tmp[i]
        ans += (tmp[0] +1) * tmp[k] 
        return ans
