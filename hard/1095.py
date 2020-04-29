class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        lenth = mountain_arr.length()
        if lenth <3:
            return -1
        
        def check(start, end):
            mid = (start + end) // 2
            if start >= end:
                return mid
            if mountain_arr.get(mid-1) < mountain_arr.get(mid) > mountain_arr.get(mid+1):
                return mid
            elif mountain_arr.get(mid-1) > mountain_arr.get(mid):
                return check(start, mid)
            else:
                return check(mid, end)
        mid = check(0, lenth)  
        
        def find(start, end):
            nonlocal target
            mid = (start + end) // 2 
            t = mountain_arr.get(mid)
            if t == target:
                return mid
            if start >= end or mid == start or mid == end: 
                return -1
            if t > target:
                return find(start, mid)
            else:
                return find(mid, end)
        
        ans = find(0, mid+1) 
        if ans != -1 :
            return ans
        def find2(start, end):
            nonlocal target
            mid = (start + end) // 2 
            t = mountain_arr.get(mid)
            if t == target:
                return mid
            if start >= end : 
                return -1
            if t < target:
                return find(start, mid)
            else:
                return find(mid, end)
        
        ans = find2(mid+1, lenth) 
        return ans
