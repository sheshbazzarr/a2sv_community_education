class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total_cost = 0
        output = 0
        for cost in costs:
            if total_cost + cost <= coins:
                total_cost += cost
                output += 1
            else:
                break

        return output
