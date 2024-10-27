class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2
        
        for i in range(n):
            total_cost += costs[i][0] 
            total_cost += costs[i + n][1]  
        
        return total_cost
