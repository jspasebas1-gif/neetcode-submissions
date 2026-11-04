class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r+=1
            else:
                profit = max((prices[r] - prices[l]), profit)
                r+=1
        return profit

       