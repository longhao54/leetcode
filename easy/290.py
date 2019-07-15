'''

给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。

这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false

'''

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        String = str.split()
        if len(pattern) != len(String):
            return False
        if len(set(pattern)) != len(set(String)):
            return False
        check_dict = {}
        for p, s in zip(pattern, String):
            if p not in check_dict:
                check_dict[p] = s
            elif check_dict[p] != s:
                return False
        return True

a = Solution()
print(a.wordPattern("abba","dog dog dog dog"))