class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        i = 0
        res = []
        while deck:
            if i % 2 == 0:
                res.insert(0, deck.pop())
            else:
                res.insert(0, res.pop())
            i += 1
        return res
