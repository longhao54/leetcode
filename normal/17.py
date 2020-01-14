class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dt = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        lenth = len(digits)
        if len(digits) == 0:
            return []
        def backtrade(index, t):
            if index == lenth:
                result.append(t)
                return
            for i in dt[digits[index]]:
                backtrade(index+1, t+i)
        for i in dt[digits[0]]:
            backtrade(1, i)
        return result
