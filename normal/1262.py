class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        one = []
        two = []
        s = 0
        for i in nums:
            s += i
            if i %3 == 1:
                one.append(i)
            elif i % 3 == 2:
                two.append(i)
        one.sort()
        two.sort()
        if s % 3 == 0:
            return s
        if s % 3 == 1:
            if len(two) >= 2:
                return s - min(two[0]+two[1], one[0])
            return s - one[0]
        else:
            if len(one) >= 2:
                return s - min(one[1]+one[0], two[0])
            return s - two[0]    
