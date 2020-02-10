# 不想写了 看的答案
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        jk=[cells]
        N = N%14
        for m in range(14):
            k=[None]*8
            k[0] = 0
            k[-1] = 0
            for i in range(1,7):
                if (jk[m][i-1] == 0 and jk[m][i+1]  ==0)or (jk[m][i-1] ==1 and jk[m][i+1] == 1):
                    k[i] = 1
                else:
                    k[i] = 0
            jk.append(k)
        if N !=0:
            return jk[N]
        else:
            return jk[14]
