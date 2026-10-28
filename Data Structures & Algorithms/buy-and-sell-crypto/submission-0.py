class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diffs = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        maximum = 0
        currSum = 0
        for price in diffs:
            if price > price + currSum:
                currSum = price
            else:
                currSum += price
            if currSum > maximum: maximum = currSum
        return maximum