class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        als=','.join(words)
        res=[]
        for s in words:
            if als.count(s)!=1:
                res.append(s)
        return res
