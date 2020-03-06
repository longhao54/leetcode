class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans = 0
        s = sum(calories[0:k])
        index = 0
        if s < lower:
            ans -= 1
        elif s > upper:
            ans += 1
        l = len(calories) - k 
        while index < l:
            s -= calories[index]
            s += calories[index+k]
            index += 1
            if s < lower:
                ans -= 1
            elif s > upper:
                ans += 1
        return ans

# 最快答案
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        s = len(calories)
        if s < k:
            return 0
        score = 0
        calories = [0] + calories
        from functools import reduce
        tmp = reduce(lambda x,y:x+y, calories[:k])
        k -= 1


        for i in range(1, s - k + 1):
            tmp = tmp - calories[i - 1] + calories[i + k]
            #print(i, tmp)
            if tmp > upper:
                score += 1
            elif tmp < lower:
                score -= 1
        return score
