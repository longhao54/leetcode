# 弱智题 中文翻译有问题 应该是返回第一次反转操作后所有可能的状态



class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        ans=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]=='+':
                ans.append(s[:i]+'--'+s[i+2:])
        return ans

