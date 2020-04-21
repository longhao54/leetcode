class FileSystem:

    def __init__(self):
        self.ans = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.ans or len(path.split("/")) != 2 and "/".join(path.split("/")[0:-1]) not in self.ans:
            return False
        
        self.ans[path] = value
        return True

    def get(self, path: str) -> int:
        return self.ans.get(path, -1)
