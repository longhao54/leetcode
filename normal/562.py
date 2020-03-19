class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        ans = 0
        if not M:
            return ans
        t = [[0, 0, 0]] * len(M[0])
        l = len(t) -1
        for line in M:
            tmp = []
            for i, v in enumerate(line):
                if v == 1:
                    if i == 0 and i != l:
                        tmp.append([t[i][0]+1, 1, t[i+1][2]+1])
                    elif i == l:
                        tmp.append([t[i][0]+1, t[i-1][1]+1, 1])
                        
                    else:
                        tmp.append([t[i][0]+1, t[i-1][1]+1, t[i+1][2]+1])
                    if i != 0:
                        line[i] += line[i-1]
                    ans = max(tmp[i]+[line[i], ans])
                else:
                    tmp.append([0,0,0])
            t = tmp.copy()
        return ans
