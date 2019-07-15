class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        index = 1
        lenth = len(chars)
        if lenth > 1:
            count = 1
            check_string = chars[0]
            while index < lenth:
                if chars[index] == check_string:
                    count += 1
                    chars.pop(index)
                    lenth -= 1
                else:
                    if count != 1:
                        for i in list(str(count)):
                            chars.insert(index, i)
                            lenth += 1
                            index += 1
                    check_string = chars[index] if index < lenth else chars[index-1]
                    index += 1
                    count = 1
            if count > 1:
                for i in list(str(count)):
                            chars.append(i)

    def fast(self, chars):
        if not chars:
            return 0
        chars.append(None)
        it = iter(chars)
        n, cnt, k = 0, 1, next(it)
        for ch in it:
            if ch == k:
                cnt += 1
            elif cnt == 1:
                chars[n] = k
                n += 1
                k = ch
            else:
                s = str(cnt)
                chars[n] = k
                for i, c in enumerate(s):
                    chars[n + i + 1] = c
                n += len(s) + 1
                cnt = 1
                k = ch
        return n
