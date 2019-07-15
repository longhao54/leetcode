class Solution:
    def nthUglyNumber(self, n: int) -> int:
        check = set()
        start = 1
        temp = [1]
        ans = []
        while ans.__len__() < n:
            m = min(temp)
            ans.append(m)
            temp.remove(m)
            a, b, c = 2 * m, 3*m, 5*m
            if a not in check:
                check.add(a)
                temp.append(a)
            if b not in check:
                check.add(b)
                temp.append(b)
            if c not in check:
                check.add(c)
                temp.append(c)
        return ans[-1]


    # 这个是答案里最快的方法 . 但是我现在还没有想清楚 为什么 是 31, 20 14
    @classmethod
    def add_num(cls):
        cls.ugly_list = []
        for i in range(31):
            for j in range(20):
                for h in range(14):
                    cls.ugly_list.append((2 ** i) * (3 ** j) * (5 ** h))
        cls.ugly_list.sort()

    def nthUglyNumber(self, n: int) -> int:
        try:
            return Solution.ugly_list[n - 1]
        except:
            Solution.add_num()
            return Solution.ugly_list[n - 1]
