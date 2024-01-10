'''
You are given an array prices where prices[i] is the price of a given
stock on the ith day

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock


Return the maximum profit you can achieve from this transation.
If you cannot achieve any profit, return 0

You must buy before you sell

'''


class Solution:
    def maxProfit(self, prices):
        # Initialize Pointers
        l, r = 0, 1 # left is buy, right is sell
        max_profit = 0 # will be updated progressively
        # keep iterating through the array
        while r < len(prices):
            # check if it is a profitable trade
            if prices[l] < prices[r]: # this is a profitable trade
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit) #get the greatest of the two
            else:
                l = r
            r += 1
        return max_profit

def main():
    print()
    prices = [7,1,5,3,6,4]
    # Expected output is 5
    test_case = Solution()
    print(test_case.maxProfit(prices))


if __name__ == '__main__':
    main()

