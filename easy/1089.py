class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr) 
        index = 0
        while index < l-1:
            if arr[index] != 0:
                index += 1
            else:
                t = arr[index+1: l-1]
                arr[index+1] = 0
                arr[index+2:] = t
                index+= 2
        
