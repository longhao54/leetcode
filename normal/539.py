class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        for index,time in enumerate(timePoints):
            h = int(time.split(":")[0])
            m = int(time.split(":")[1])
            time = h*60 + m
            timePoints[index] = time
        
        if len(set(timePoints)) != len(timePoints):
            return 0
        timePoints.sort()
        start = timePoints[0]
        timePoints.append(start+1440)
        print(timePoints)
        for index in range(0, len(timePoints)-1):
            a = timePoints[index]
            b = timePoints[index+1]
            if abs(b - a) > 720:
                timePoints[index] = 1440 +a -b
            else:
                timePoints[index] = abs(b-a)
        return min(timePoints)
