class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        ret = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i-1] < duration:
                ret += timeSeries[i] - timeSeries[i-1]
            else:
                ret += duration
        
        ret += duration        
        return ret
