class Solution:
    def toHexspeak(self, num: str) -> str:
        num_hex = hex(int(num))[2:]
        transform = {
            "0": "O",
            "1": "I",
            "a": "A",
            "b": "B",
            "c": "C",
            "d": "D",
            "e": "E",
            "f": "F",
        }
        
        ans = ""
        for ch in num_hex:
            if ch not in transform:
                return "ERROR"
            ans += transform[ch]
        return ans
