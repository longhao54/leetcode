class Solution:
    def fast(self, S):
        left = 0
        right = len(S)
        A = []
        for i in S:
            if i == 'I':
                A.append(left)
                left += 1
            else:
                A.append(right)
                right -= 1
        A.append(right)
        return A

    def diStringMatch(self, S):
        ans = [ i for i in range(len(S)+1)]
        A = []
        for i in S:
            if i == "I":
                A.append(ans.pop(0))
            else:
                A.append(ans.pop())
        A.append(ans.pop())
        return A
