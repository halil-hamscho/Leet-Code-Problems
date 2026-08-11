'''
initialize prev_1, prev_2 with the costs of the first and second steps

using an iterative approach, we iterate over the remaining steps (starting from the third step)
for each step i, it calculates the minimum cost to reach that step
by taking the minimum of the costs of the previous steps and adding the current steps cost

it updates prev_1 prev_2 accordingly for the next iteration

Time Complexity: the function iterates over each step in the cost list once, performing 
costnant time operations within each iteration. O(N) where N is the number of steps in the stairs

Space: O(1)

'''

class Solution:
    def minCostClimbingStairs(self, cost):
        # Since the cost is based on two decisions (1 step) or (2 steps)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-2], cost[-1])

def main():
    result = Solution()
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(result.minCostClimbingStairs(cost))

if __name__ == "__main__":
    main()