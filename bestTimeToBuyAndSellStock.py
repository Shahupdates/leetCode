class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        You are given an array 'prices' where 'prices[i] is the price of a given stock on the i'th day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sel that stock.
        Return the maximum profit you can achieve from this transaction, if you cannot achieve any profit return 0.
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
          min_price = min(min_price, price)
          max_profit = max(max_profit, price - min_price)

        return max_profit

    
    """
    Example:
    Lets say we have an example prices array: 
    [7, 1, 5, 3, 6, 4]
    1. Iterating through the price array, at price 7, we update min_price to  and max_profit to 0 
    2. At price 1, update min_price to 1 and max_profit to 4
    3. At price 3, update min_price to 1 and max_profit to 4
    4. At price 5, update min_price to 1 and max_profit to 4
    5. At price 3, update min_price to 1 and max_profit to 3-1 = 2
    6. At price 6, update min_price to 1 and max_profit to (6-1) = 5
    7. At price 4, update min_price to 1 and max_profit to 3, (4-1) = 3
    8. Return max_profit which is 5 in this case.
    9. If no profit i possible, function will return  0.
    """
