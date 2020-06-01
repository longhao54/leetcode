class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        r1, r2 = sys.maxsize, sys.maxsize
        for n in nums :
            if n <= r1 : r1 = n
            elif n <= r2 : r2 = n
            else : return True
        return False
