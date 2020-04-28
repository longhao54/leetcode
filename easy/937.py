class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digs, ltrs, iltrs = [], [], {}
        for log in logs:
            i = log.find(' ') + 1
            if log[i].isdigit():  # 判断是否字母/数字
                digs += [log]
            else:
                iltrs[log] = i   # 记录第一个空格出现的位置
                ltrs += [log]
        return sorted(ltrs, key = lambda log: [log[iltrs[log]: ], log[: iltrs[log]]]) + digs    


