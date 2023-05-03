"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i!= k, and j != k, and nums[i] + nums[j] = nums[k] == 0
Notice that the solution set must not contain duplicate triplets

This solution has a time complexity of O(n^3) because its not efficient for large input arrays, 
2-pointer approach is more efficient with O(n^2)
"""

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    #code first initialies an empty result list
    res = []
    #then iterates over all possible triplets of elements in the input array
    for i in range (len(nums) - 2): #iterate over the first n-2 elements
      for j in range (i + 1, len(nums) - 1): #iterate over the elements after i
        for k in range (j+1, len(nums)): #iterate over the elements after j
         #checking if the sum of the triplet is 0
         if nums[i] + nums[j] + nums[k] == 0: 
            #if it is 0, then sort the triplet
             triplet = sorted([nums[i], nums[j], nums[k]])
             #if the triplet is not in the result list, add it to the result list
             if triplet not in res:                 
              res.append(triplet)
    #return the result list if triplet is already in the result list
    return res


                            
