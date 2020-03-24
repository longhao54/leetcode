class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        t = set()
        start = 0
        folder.sort()
        while start < len(folder):
            t = folder[start]+"/"
            n = start + 1
            while n < len(folder):
                if folder[n].startswith(t):
                    folder.pop(n)
                else:
                    break
            start += 1
        return folder
