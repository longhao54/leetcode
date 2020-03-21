from collections import defaultdict
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        a = defaultdict(int)
        for i in arr:
            a[i]+= 1
        for i in a:
            if i == 0 and a[0]>= 2:
                return True
            if i*2 in a and i != 0:
                return True
        return False
