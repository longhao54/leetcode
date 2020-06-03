class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        c = False
        def check(word):
            nonlocal c
            if c or not word:
                c = True
                return ""
            for i in wordDict:
                if word.startswith(i):
                    l = len(i)
                    lenth = l
                    while word[lenth:].startswith(i):
                        lenth += l
                    check(word[lenth:])
        check(s)
        return c
