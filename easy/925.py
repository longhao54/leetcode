class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_dict = self.check([], name)
        name_typed = self.check([], typed)
        if len(name_dict) != len(name_typed):
            return False
        for i, j in zip(name_dict, name_typed):
            if j < i:
                return False
        return True
    
    def check(self, ndict, name):
        last = "0"
        for i in name:
            if i != last:
                ndict.append(1)
                last = i
            else:
                ndict[-1] += 1
        return ndict

    def faster(self, name: str, typed:str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)
