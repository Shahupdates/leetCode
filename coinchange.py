class Solution:
    """
    You are given an integer array coins, representing coins of different denominations
    and an integer amount representing a total amount of money
    Return the fewest number of coins that you need to make up that amount

    If the amount of money cannot be made by any combination of the coins: return -1

    You may assume that you have an infinite number of each kind of coin
    
    The coinChange function takes an integer array coins and an integer amount as input
    and returns the fewest number of coins needed to make up the amount, if its not
    possible to make up the amount using the available coins, returns -1
    """
    def coinChange(self, coins: List[int], amount: int) -> int:

        # assume that you have an infinite number of each kind of coin
        # dp list is initialized with float('inf') for all indices from 0:amount
        # dp[i] represents the fewest number of coins needed to make up the amount i
        dp = [float('inf')] * (amount + 1) # why add one??


        # the value of dp[0] is set to 0 because it takes 0 coins to make up an amount of 0
        dp[0] = 0

        # the outer loop iterates over the available coin denominations in the coins array
        for coin in coins:
            # the inner loop iterates over the possible amounts starting from the value
            # of the current coin denominations 'coin' up to the 'amount'
            for i in range(coin, amount + 1): # why add one??

                #this line updates the value of dp[i] by taking the minimum between the current value
                #of dp[i], and the value of dp[i - coin] plus 1, this ensures that we consider all
                #possible combinations of coins to make up the amount i, and choose the fewest number of coins
                dp[i] = min(dp[i], dp[i - coin] + 1) # why add one??


        #after the loops finish if the value of dp[amount] remains float(inf) then it wasnt possible
        #to make up the amount using the available coins, in this case we return -1
        if dp[amount] == float('inf'):
            return -1
        #otherwise we return the value of dp[amount] as the fewest number of coins needed 
        #to make up the amount
        else:
            return dp[amount]
            
