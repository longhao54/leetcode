class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        i, j = 0, 0
        ans = ""
        for ch in list(target):
            row, col = int(ord(ch) - ord('a')) // 5, int(ord(ch) - ord('a')) % 5
            while j > col:
                j -= 1
                ans += "L"
            while i > row:
                i -= 1
                ans += "U"
            while j < col:
                j += 1
                ans += "R"
            while i < row:
                i += 1
                ans += "D"
            ans += '!'
        return ans
