class MagicDictionary:

    def __init__(self):
        self.dup = {}
        self.tire = {}

    def buildDict(self, dict: List[str]) -> None:
        for word in dict:
            self.dup[word] = 1
            dp = self.tire
            for w in word:
                if w not in dp:
                    dp[w] = {}
                dp = dp[w]
            dp["end"] = {}
        
    def search(self, word: str) -> bool:
        ans = 0
        def check(word, dp):
            nonlocal ans
            if not word:
                if "end" in dp :
                    ans += 1
                return ""
            if not word:
                return ""
            if word[0] == ".":
                for i in dp:
                    check(word[1:], dp[i])
            else:
                if word[0] in dp:
                    check(word[1:], dp[word[0]])
                else:
                    return ""
        
        for index, _ in enumerate(word):
            check(word[0:index]+"."+word[index+1:], self.tire)
            if word not in self.dup and ans > 0:
                return True
        return ans > 0 if word not in self.dup else ans > len(word)
