class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        dic = collections.defaultdict(int)
        ans = []
        for name in names:
            if dic[name] == 0:
                ans.append(name)
            else:
                k = dic[name]
                while True:
                    tmpName = name + '(' + str(k) + ')'
                    if dic[tmpName] == 0:
                        ans.append(tmpName)
                        dic[tmpName] += 1
                        break
                    k += 1
            dic[name] += 1
        return ans
