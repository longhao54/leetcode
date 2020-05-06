class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        last = paths[0][0]
        tmp = {k:v for k, v in paths}
        while last in tmp:
            last = tmp[last]
        return last
