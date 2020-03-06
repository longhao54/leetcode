from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        t = defaultdict(int)
        t["zz"] = 0
        left, right = 0, 0 
        l = len(s)
        while l -left > ans and right < l:
            if sum(t.values()) - max(t.values()) <= k:
                ans = max(ans, sum(t.values()))
                t[s[right]] += 1
                right += 1
            else:
                tmp = s[left]
                t[tmp] -= 1
                if t[tmp] == 0:
                    t.pop(tmp)
                left += 1
        if sum(t.values()) - max(t.values()) <= k:
            ans = max(ans, sum(t.values()))
        return ans


# 最快答案
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        left = maxcount = 0
        ans = 0
        for i in range(len(s)):
            count[s[i]] += 1
            maxcount = max(maxcount, count[s[i]])
            if i-left+1 > maxcount + k:
                count[s[left]] -= 1
                left += 1
            # ans = max(ans, i-left+1)
        return len(s)-left
