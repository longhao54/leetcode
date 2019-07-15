#!/usr/bin/env python

'''

统计所有小于非负整数 n 的质数的数量。
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

'''

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pri_list = set()
        # def numCheck(n):
        #     print(pri_list)
        #     for num in pri_list:
        #         if n % num == 0:
        #             return False
        #     pri_list.add(n)
        #
        # if n <= 2:
        #     return 0
        # for i in range(3, n, 2):
        #     numCheck(i)
        # print(pri_list)
        # return len(pri_list)+1

        if n <= 2:
            return 0
        t_dict = {}
        # for i in range(3,n,2):
        #     t_dict[i] = True
        # for i in range(3, n, 2):
        #     if not t_dict[i] :
        #         print(i)
        #         continue
        #     for j in range(2,n):
        #         val = i * j
        #         if val < n:
        #             t_dict[val] = False
        #         else:
        #             break

        c = n // 2 -1if n %2 != 0 else (n -1 ) // 2
        for i in range(3, n, 2):
            Max = n // i
            for j in range(3, Max +1, 2):
                val = i * j
                # if val != n :
                t_dict[val] = False
        if n not in t_dict:
            return c - len(t_dict) +1
        else:
            return c - len(t_dict) + 2

        


a = Solution()
print(a.countPrimes(8))
