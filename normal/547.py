class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        t = []
        tmp = {}
        def check(x):
            if x not in tmp or x == tmp[x]:
                return x
            return check(tmp[x])    
        
        l = len(M)
        for i in range(l):
            for j in range(i+1, l):
                if M[i][j] == 1:
                    t.append([i, j])
        
        for x, y in t:
            x, y = check(x), check(y)
            tmp[x] = y

        ans = set()
        for i in range(l):
            ans.add(check(i))

        return len(ans)
