class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            profit_now=prices[i]-min_price_so_far
            max_profit=max(max_profit,profit_now)
            min_price_so_far=min(min_price_so_far,prices[i])
        return max_profit
        