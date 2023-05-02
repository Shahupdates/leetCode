"""
Given an integer n, return an array ans of length n + 1, such that for each i, ans[i] is the number of
1s in the binary representation of i
"""

class Solution:
  # we can use dynamic programming to solve this problem, we start by initializing the
  # an array dp of length n+1 with all elements set to 0
  # then we loop through the integers from 1 to n+1
  # and for each integer i, we set dp[i] to dp[i>>1] (which is the # of 1 bits in the binary representation of i)
  def countBits(self, n: int) -> List[int]:
    dp = [0] * (n+1)
    for i in range(1, n+1):
      dp[i] = dp[i >> 1] + (i & 1)
      # which is 1 if the LSB of i is a "1" and 0 otherwise because i>>1 = i/2 , 
      # so # of 1 bits in i>>1 is same as number of 1 bits in i without the LSB
    return dp
