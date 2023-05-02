"""
Given an integer array nums return true if any value appears at least twice in the array, and 
return false, if every element is distinct
Since sets have O(1) for checking membership and adding elements,
the time complexity of this algorithm is O(n), where n is the length of the input list nums
"""

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set() #empty set seen to store the numbers we have seen so far
    for num in nums:
      if num in seen:
        return True #if nums contains any duplicates
      seen.add(num) #if its not in the seen set we add it using the add method 
    #if we've iterated through all the numbers in nums without finding a duplicate, return false
    return False
