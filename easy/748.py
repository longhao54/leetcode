class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        L = ''
        for c in licensePlate.lower():
            if c in 'abcdefghijklmnnopqrstuvwxyz':
                L += c
        res = ''
        for c in words:
            if res == '' or len(c) < len(res):
                S = list(c)
                for i in L:
                    if str(i) in S:
                        S.remove(i)
                    else:
                        break
                else:
                    res = c
        
        return res
