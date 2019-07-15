class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        import re
        source = '\n'.join(source)
        s = {'//.*', r'/\*[\s\S]*?\*/'}
        while s:
            a = None
            for i in s:
                m = re.search(i, source)
                if not m:
                    s.remove(i)
                    break
                m = m.span()
                if not a or m[0] < a[0]:
                    a = m
            else:
                source = source[:a[0]] + source[a[1]:]
        return [i for i in source.split('\n') if i]
