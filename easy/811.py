from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        temp = defaultdict(int)
        ans = []
        for i in cpdomains:
            c, d = i.split()
            d = d.split(".")
            for i in range(len(d)):
                temp[".".join(d[i::])] += int(c)
        for k, v in temp.items():
            ans.append("{} {}".format(v, k))
        return ans 
