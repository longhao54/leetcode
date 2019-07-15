class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        List = []
        for index, word in enumerate(text):
            if index > len(text) - 3:
                break
            if word == first and text[index+1] == second:
                List.append(text[index + 2])  
        return List

