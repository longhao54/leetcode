class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: (x[0]-x[1]))  # 计算去A地和去B低的费用差，然后按照费用差排序
        length_costs = len(costs)
        result = 0
        result += sum([i[0] for i in costs[:length_costs//2]])  # 前半部分去A地
        result += sum([i[1] for i in costs[length_costs//2:]])  # 后半部分去B地
        return result
