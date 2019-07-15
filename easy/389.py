'''

给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。



示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

'''


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum_s, sum_t = 0, 0
        for i, j in zip(s + "a", t):
            sum_s += ord(i)
            sum_t += ord(j)
        return chr(sum_t - sum_s + ord("a"))

a = Solution()
print(a.findTheDifference("asdf","asdfe"))