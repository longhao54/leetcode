from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        a_b, b_b = [], []
        t = {}
        for index, value in enumerate(guess):
            if value == secret[index]:
                a+=1
            else:
                a_b.append(secret[index])
                b_b.append(value)
        for i in b_b:
            if i in a_b:
                b+=1
                a_b.remove(i)
        return "{}A{}B".format(str(a), str(b))
