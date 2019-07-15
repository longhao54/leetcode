class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for index, value in enumerate(A):
            value = str(value[::-1]).replace("[","").replace("]","").replace(", ","")
            value = int("1"*(len(value)+1)) - int(value)
            ans = []
            for i in str(value)[1:]:
                ans.append(int(i))
            A[index] = ans
        return ans
