import math
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        max_x = int(math.log(bound, x))+1 if x != 1 else 1
        max_y = int(math.log(bound, y))+1 if y != 1 else 1
        ans = set()
        for i in range(max_x):
            for j in range(max_y):
                a = x**i + y**j
                if a > bound:
                    break
                ans.add(a)
        return list(ans)

    def fast(self, x, y, bound):
        res_set = set()
        for i in range(bound):
            tmp1 = x ** i 
            if tmp1 > bound:
                break
            for j in range(bound):
                tmp2 = y ** j
                tmp = tmp1 + tmp2
                if tmp > bound:
                    break
                res_set.add(tmp)
        return res_set
