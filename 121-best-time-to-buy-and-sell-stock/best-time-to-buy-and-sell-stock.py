class Solution:
    def maxProfit(self,prices):
        n=len(prices)
        profit=0
        mini=prices[0]
        for i in range(n):
            diff=prices[i]-mini
            profit=max(profit,diff)
            mini=min(mini,prices[i])

        return profit