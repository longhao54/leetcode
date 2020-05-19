class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n, d = len(mat), len(mat[0]), collections.defaultdict(list)
        for i, j in itertools.product(range(m), range(n)):
            d[i - j].append(mat[i][j])
        d = {k: iter(sorted(v)) for k, v in d.items()}
        for i, j in itertools.product(range(m), range(n)):
            mat[i][j] = next(d[i - j])
        return mat
