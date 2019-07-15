class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        a = {len(tuple(i)) for _, i in groupby(sorted(deck))}
        if not a or any(map(lambda x: x < 2, a)):
            return False
        a = sorted(a)
        for i in range(2, a[0] + 1):
            if all(map(lambda x: x % i == 0, a)):
                return True
        return False
