class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = 0
        for nums in triangle:
            ans += min(nums)
        return ans
