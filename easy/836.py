class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        xmin, ymin, xmax, ymax = rec1
        amin, bmin, amax, bmax = rec2
        return amin < xmax and bmin < ymax and amax > xmin and bmax > ymin 
