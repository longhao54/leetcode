from collections import defaultdict
class Solution:
    def numsSameConsecDiff(self, N, K):
        if N == 1:
            return [1,2,3,4,5,6,7,8,9,0] 
        if K == 0:
            return [ int(str(i)*N) for i in range(1,10) ]
        rl = defaultdict(list)
        for i in range(10):
            if i - K >= 0:
                rl[i].append(i-K)
            if i + K <= 9:
                rl[i].append(i+K)
        ans = []
        for i in range(1, 10):
            temp = [i]
            count = 1
            while count < N:
                lenth = temp.__len__()
                for j in temp[0:lenth]:
                    for num in rl[int(str(j)[-1])]:
                        if j*10 + num >= 10 ** (count-1):
                            temp.append(j*10+num)
                temp = temp[lenth::]
                count += 1
            ans += temp
        return ans
