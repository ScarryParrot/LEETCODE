class Solution:
    def maxProfit(self, prices):
        profit = 0
        minp = float('inf')
        
        for i in prices:
            if i < minp:
                minp = i
            
            # Calculate the potential profit if selling at the current price
            diff = i - minp
            
            # Update the maximum profit
            profit = max(profit, diff)
        
        return profit