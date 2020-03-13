class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        ans = None
        place = {}
        for i in regions:
            p = i[0]
            for j in i[1:]:
                place[j] = p

        s = set()
        s.add(region1)
        while region1 in place:
            t = place[region1]
            s.add(t)
            region1 = t
        
        while region2 in place:
            if region2 in s:
                return region2
            region2 = place[region2]
        return region2
