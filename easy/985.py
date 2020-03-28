class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s= sum([i for i in A if i % 2 == 0])
        ans = []
        for i in queries:
            val, index = i
            t = A[index]
            if t % 2 == 0:
                if val % 2 == 0:
                    s += val
                else:
                    s -= t
            else:
                if val % 2 == 1:
                    s += t+val
            A[index] += val
            ans.append(s)
        return ans
