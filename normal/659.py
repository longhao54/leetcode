# 差点超时的解法
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        t = []
        start = 0
        last = nums[0]
        for i in nums:
            c = False
            for j in t[::-1]:
                if j[-1] +1 == i:
                    c = True
                    j.append(i)
                    break
            if not c:
                t.append([i])
                start += 1
        for i in t:
            if len(i) >= 3:
                continue
            else:
                return False
        return True
                

class Solution(object):
    def isPossible(self, nums):
        count = collections.Counter(nums)
        tails = collections.Counter()
        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False
            count[x] -= 1
        return True

