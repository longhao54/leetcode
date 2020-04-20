import collections
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans=0
        for i in points:
            dis=[]
            for j in points:
                dis.append((j[1]-i[1])**2+(j[0]-i[0])**2)
            for j,k in collections.Counter(dis).items():
                if j!=0 and k>=2:ans+=k*(k-1)
        return ans
