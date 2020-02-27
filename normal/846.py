from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        count = defaultdict(int)
        s = set(hand)
        s = sorted(list(s))
        for i in hand:
            count[i] += 1
        while len(s) >= W:
            t = s[0]
            for i in range(W):
                if count[t+i] >= 1:
                    count[t+i] -= 1
                else:
                    return False
                if count[t+i] == 0:
                    s.remove(t+i)
        if len(s)!= 0:
            return False
        return True


# 最快答案
class Solution:
    def isNStraightHand(self, hand: List[int], w: int) -> bool:
        lst_len = len(hand)
        if lst_len % w != 0:
            return False
        rem_dict = {i : 0 for i in range(w)}
        for ele in hand:
            rem_dict[ele%w] += 1
        return len(set(rem_dict.values())) == 1
