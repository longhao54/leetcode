class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        count = 0
        last = nums[0]
        s = 0
        for i in nums[1:]:
            if i - last != 1:
                count = i-last-1
                if count >= k:
                    break
                elif k > count:
                    k -= count
            last = i
        return last + k
