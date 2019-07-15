#!/bin/bash
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        final, check = [], {}
        for i in range(60):
            check[i] = 0

        for i in time:
            t_left = i % 60
            check[t_left] += 1
            final.append(t_left)

        if len(final) < 2 and 0 not in final:
            return 0
        final = set(final)
        count = 0
        print(final)
        if 0 in final and check[0] >= 2:
            for i in range(1,check[0]):
                count += i
            final.remove(0)
        if 30 in final and check[30] >= 2:
            for i in range(1,check[30]):
                count += i
            final.remove(30)
        temp = 0
        
        for i in final:
            if 60 - i in final:
                temp = temp + check[i]*check[60-i]
        print(temp, count, final)
        return count + temp//2

    def fast(self, time):
        res = 0
        d = [0] * 60
        for t in time:
            d[t % 60] += 1
        res += max(0, d[0] * (d[0] - 1) // 2)
        res += max(0, d[30] * (d[30] - 1) // 2)
        for i in range(1, 30):
            res += d[i] * d[60 - i]
        return res
