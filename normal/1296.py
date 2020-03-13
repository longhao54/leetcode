# 弱智方法 超时了
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        num, nums_c = [], []
        nums.sort()
        for i in nums:
            index = 0
            c = True
            while index < len(num):
                if nums_c[index] < k and num[index]+1 == i :
                    c = False
                    num[index] += 1
                    nums_c[index] += 1
                    if nums_c[index] == k:
                        num.pop(index)
                        nums_c.pop(index)
                    break
                index += 1
            if c:
                num.append(i)
                nums_c.append(1)
        for i in nums_c:
            if i != k:
                return False
        return True


# 贴边
from collections import defaultdict
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        numd = defaultdict(int)
        for i in nums:
            numd[i] += 1
        n = sorted(numd.keys())
        while n:
            i = n.pop(0)
            c = numd[i]
            numd[i] = 0
            for j in range(i+1, i+k):
                if numd[j] > c:
                    numd[j] -= c
                elif numd[j] == c:
                    numd[j] = 0
                    n.remove(j)
                else:
                    return False 
        return True

# 这就快了很多
from collections import defaultdict
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        numd = defaultdict(int)
        for i in nums:
            numd[i] += 1
        while numd:
            i = min(numd)
            c = numd[i]
            numd.pop(i)
            for j in range(i+1, i+k):
                if numd[j] > c:
                    numd[j] -= c
                elif numd[j] == c:
                    numd.pop(j)
                else:
                    return False
        return True
