class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = []
        start, end = 0, len(height)-1
        startnum, endnum = height[start], height[end]
        while start < end:
            ans.append( min(endnum, startnum) * ( end-start ) )
            if startnum > endnum:
                end -= 1
                endnum = height[end]
            else:
                start += 1
                startnum = height[start]
        return max(ans)
