class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = float("-inf")
        m = arrays[0][0]
        ma = arrays[0][-1]
        for i in arrays[1:]:
            ans = max(ans, abs(i[-1]-m), abs(i[0]-ma))
            m = min(i[0], m)
            ma = max(i[-1], ma)
        return ans
