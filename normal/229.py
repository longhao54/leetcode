from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = defaultdict(int)
        c = len(nums) // 3
        ans = []
        for i in nums:
            if i in ans:
                continue
            t[i] += 1
            if t[i] > c:
                ans.append(i)
        return ans
