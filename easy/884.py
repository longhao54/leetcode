class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        ans = []
        noans = []
        B = B.split()
        A = A.split()
        for string in A:
            if string not in B and string not in noans:
                ans.append(string)
            elif string in noans and string in ans:
                ans.remove(string)
            noans.append(string)
        for string in B:
            if string not in A and string not in noans:
                ans.append(string)
            elif string in noans and string in ans:
                ans.remove(string)
            noans.append(string)
        return ans


    def faster(self, A: str, B:str) -> List[str]:
        c = collections.Counter((A + " " + B).split(" "))
        return [v for v in c if c[v] == 1]
