class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        myMin = prices[0]
        curr_val = 0
        for i in range(len(prices)):
            myMin = min(myMin, prices[i])
            curr_val = max(curr_val, prices[i]-myMin)
        return curr_val