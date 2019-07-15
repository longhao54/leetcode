class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        self.ans = {}
        for i in A[0]:
            if i in self.ans:
                self.ans[i] += 1
            else:
                self.ans[i] = 1
        if len(A) != 1:
            for word in A[1:]:
                self.check(word)
                if not self.ans :
                    return []
        final = []
        for k, v in self.ans.items():
            for i in range(v):
                final.append(k)
        return final

    def check(self, word):
        ans = {}
        for k, v in self.ans.items():
            if k in word:
                ans[k] = min([v, word.count(k)])
        self.ans = ans

    def fast(self, A):
        l = []
        string = set(A[0])
        for i in string:
            l += [i]*min(list(map(lambda x:x.count(i),A)))
        return l
