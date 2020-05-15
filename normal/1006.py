class Solution:
    def clumsy(self, N: int) -> int:
        temp = [0, 1, 2, 6, 7]
        if N <= 4:
            return temp[N]
        res = N + 1 + N - 3
        N -= 4

        four_times = N // 4
        remainder = N % 4

        if remainder:
            return res + -4 * four_times - temp[remainder]
        else:
            return res + -4 * (four_times - 1) - 5
