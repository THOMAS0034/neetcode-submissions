class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit_loss=[]
        for i in range(1,len(prices)):
            sublist_prices = prices[:i]
            sell_val = min(sublist_prices)
            profit_loss.append(prices[i] - sell_val)
        if max(profit_loss) < 0:
            return 0
        return max(profit_loss)
        