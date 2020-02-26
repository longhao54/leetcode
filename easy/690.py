class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        self.d = {}
        for i in employees:
            p, point, o = i.id, i.importance, i.subordinates
            self.d[p] = [point, o]
        ans = self.check(id)
        return ans 
    def check(self, i):
        ans = self.d[i][0]
        for j in self.d[i][1]:
            ans += self.d[j][0]
            if self.d[j][1]:
                for t in self.d[j][1]:
                    ans += self.check(t)
        return ans
