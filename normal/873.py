from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        relation = { value: index for index, value in enumerate(A)}
        temp = defaultdict(lambda: 2)
        ans = 0
        for i, v in enumerate(A):
            for j in range(i):
                t = relation.get(v-A[j], None)
                if t is not None and t < j:  # 因为t 可能是0 所以不能直接 if t 然后为了index的升序 所以要保证 t < j 免得 如 7 1 6 这种形式的出现
                    t_ans = temp[j,i] = temp[t,j] +1
                    ans = max(ans, t_ans)
        return ans if ans >= 3 else 0



