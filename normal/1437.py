class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        last = -k-1
        for i, v in enumerate(nums):
            if v == 1:
                if i - last <= k:
                    return False
                last = i
        return True
