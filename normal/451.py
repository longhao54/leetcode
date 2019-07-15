class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        check = set()
        ans = {}
        for key_s, value_count in count.items():
            check.add(value_count)
            if value_count in ans:
                ans[value_count] += key_s * value_count
            else:
                ans[value_count] = key_s * value_count
        check = sorted(list(check))
        final = ""
        for i in check[::-1]:
            final += ans[i]
        return final
        

    def fast(self, s):
        from operator import itemgetter
        c = collections.Counter(s)
        l = sorted(c.items(), key=itemgetter(1), reverse=True)
        return ''.join(c*n for c, n in l)
