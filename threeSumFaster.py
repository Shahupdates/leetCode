
"""
O(n^2)
Short implementation in Python that uses a dictionary to avoid
duplicate triplets
"""

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
  #we first sort the input list nums in ascending order
  nums.sort()
  #iterate each element nums[i] in the list to the 2nd to last element
  for i in range (len(nums)-2):
  

                            
