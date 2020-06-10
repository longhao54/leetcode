class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dictance(point1,point2):
            res = (point1[0]-point2[0])*(point1[0]-point2[0]) + (point1[1]-point2[1])*(point1 [1]-point2[1]) 
            return res
        arr = [p1,p2,p3,p4]
        arr = sorted(arr,key= lambda x:(x[0],x[1]))
        return dictance(arr[0],arr[1])!=0 and dictance(arr[0],arr[1]) == dictance(arr[1],arr[3]) and dictance(arr[1],arr[3]) == dictance(arr[3],arr[2]) and dictance(arr[0],arr[3]) == dictance(arr[1],arr[2])
