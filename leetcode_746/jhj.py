class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        elif len(cost) == 3:
            first_third = cost[0] + cost[2]
            second = cost[1]
            
            return min(first_third, second)
        else :
            total_cost = []
            total_cost.append(cost[0])
            total_cost.append(cost[1])

            for i in range(2, len(cost)) :
                min_sum = min(cost[i] + total_cost[i-1], cost[i] + total_cost[i-2])
                total_cost.append(min_sum)

            return min(total_cost[-1], total_cost[-2])    

"""
Runtime: 69 ms
Memory Usage: 16.6 MB
"""