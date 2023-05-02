"""
You are given an array prices where prices[i] is the price of a given stock on the ith day
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day i nthe future to sell that stock
Return the maximum profit you can achieve from this transaction, if you cannot achieve any profit, return 0
"""

class Solution:
  """
  To solve this problem, we use a simple approach where we keep track of the minimum price seen so far
  and the maximum profit that can be obtained by selling the stock on any further day.
  """
  def maxProfit(self, prices: List[int]) -> int:
    min_price = float('inf') # we initialize the minimum price to infinity and maximum profit to 0
    max_profit = 0
    for price in prices:
      if price < min_price:   #iterate through the prices and at eeach iteration, check if the current price is lower than min so far
        min_price = price #if it is we update the minimum price we've seen so far
      else:
        #otherwise we calculate the profit that can be obtained by selling the stock on the current day (current day - minimum price)
        profit = price - min_price
        if profit > max_profit
        #and update the maximum profit seen so far if this profit is greater than the current one
          max_profit = profit
        #at the end of this iteration we return the maximum profit seen so far.
     return max_profit
