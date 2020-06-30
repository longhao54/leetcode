class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        cnt, modulo = [0] * 10, [0] * 3
        s = 0
        for digit in digits:
            cnt[digit] += 1
            modulo[digit % 3] += 1
            s += digit
        
        remove_mod, rest = 0, 0
        if s % 3 == 1:
            remove_mod, rest = (1, 1) if modulo[1] >= 1 else (2, 2)
        elif s % 3 == 2:
            remove_mod, rest = (2, 1) if modulo[2] >= 1 else (1, 2)

        ans = ""
        for i in range(0, 10):
            for j in range(cnt[i]):
                if rest > 0 and remove_mod == i % 3:
                    rest -= 1
                else:
                    ans += str(i)
        if len(ans) > 0 and ans[-1] == "0":
            ans = "0"
        return ans[::-1]
