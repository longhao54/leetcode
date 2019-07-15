class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        check = False
        for i in range(s.__len__()):
            last = s[-1]
            if last == " ":
                start = i
                check = True
            s.insert(start, last)
            s.pop()
            if check:
                start += 1
                check = False
            # print(s)

    def fast(self, s):
        str[:] = list(" ".join("".join(str).split()[::-1]))
