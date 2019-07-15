class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        # A = [str(a) for a in A]
        # TF = []
        # string = ''.join(A)
        # for i in range(len(string)):
        #     if int(string[:i+1],2)%5==0:
        #         A[i] = True
        #     else:
        #         A[i] = False
        # return A
        N = []
        pref = 0
        for a in A:
            pref = (pref*2+a)%5
            N.append(not pref)
        return N
