class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        lenth = len(S)
        if lenth - len(set(S)) < 2:
            return []
        last = S[0]
        count = 1
        Max = 3
        ans = []
        for index, value in enumerate(S[1:]):
            if value == last:
                count +=1
            else:
                if count >= Max:
                    # Max = count
                    ans.append([index+1-count,index])
                count = 1
                last = value
            lastIndex = index
        # print(lastIndex, count)
        if count >= 3:
            ans.append([lastIndex-count+2,lenth-1])
        return ans

a = Solution()
print(a.largeGroupPositions("aaa"))