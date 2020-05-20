class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        length = len(arr)
        left = 0
        right = length-k
        while left<right:
            mid = (left+right)>>1
            # 让X收缩在区间内          
            if x-arr[mid] >arr[mid+k]-x:
                # x距离左边界远，收缩左边界
                left=mid+1
            else:
                # x距离右边界远，收缩右边界
                right=mid
        
        return arr[left:left+k]
