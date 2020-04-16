class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []
        def backtrace(cur='', i=0):
            if i == len(word):
                ans.append(cur)
                return
            
            backtrace(cur + word[i], i+1)
            if not (cur and cur[-1].isdigit()):
                for j in range(i, len(word)):
                    backtrace(cur+str(j-i+1), j+1)
        backtrace()
        return ans
