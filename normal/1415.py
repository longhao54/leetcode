class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 2 ** (n-1):  # 如果 k 超出数量限制，直接返回空字符串
            return ''

        k = k - 1  # 数字 -1
        number_char = str(k // 2 ** (n - 1))  # 特殊处理第一个字符
        k = k % 2 ** (n - 1)  # 取余数，进行后续操作
        
        if len(number_char) != n:  # 如果当前字符串长度不为 n ，就需要添加后续工作
            number_char += '0' * (n - len(bin(k)[2:]) - 1) + bin(k)[2:]

        # 此时，number_char 构建完成，其为一个类似二进制的字符串,例如：
        # n = 5, k = 9, munber_char = '01000'
        # n = 5, k = 8, munber_char = '00111'
        # n = 3, k = 12, munber_char = '211'
        #print(number_char)

        res = ''
        last = None
        for cur in number_char:  # 根据 number_char 构建返回的字符串
            last = get_0_or_1(cur,last)
            res += last

        return res


def get_0_or_1(cur,last):  # 这个过程可能有点跳跃，具体可以参考最后一个图中的 蓝字部分

    if last == 'a':
        return 'b' if cur =='0' else 'c'

    if last == 'b':
        return 'a' if cur == '0' else 'c'

    if last == 'c':
        return 'a' if cur == '0' else 'b'

    if last is None:  # 特殊处理第一位
        return {
            '0':'a',
            '1':'b',
            '2':'c'
        }[cur]
