class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        Max = 2400
        temp = []
        ans = {}
        A.sort()
        for i in A:
            for j in A:
                for k in A:
                    for l in A:
                        if sorted([i,j,k,l]) == A and i*1000+j*100+k*10+l < 2400 and k < 6:
                            temp.append(i*1000+j*100+k*10+l)
                            ans[i*1000+j*100+k*10+l] = str(i)+str(j)+":"+str(k)+str(l)
        if not temp:
            return ""
        Max = max(temp)
        return ans[Max]
