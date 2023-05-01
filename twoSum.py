"""
To solve this problem we can use a hash table to keep track of the indices of the numbers we have seen so far.
We can iterate through the array and for each element "num", we check if the difference (target-num) exists
in the hash table, if it does, we found the pair of numbers that add up to "target" and we return their indices..
If it doesnt', we add 'num and its index to the hash table and continue iterating
"""


def twoSum(self, nums : List[int], target: int) -> List[int]:
  seen = {}
  # we initialize an empty hash table called seen, we use the enumerate function
  # to iterate through the array "nums" along with its indices
  for i, num in enumerate(nums):
  # for each element num and index i, we calcualte the difference
    complement = target - num
    # we check if complement is already in the seen hash table, if it is were done
    if complement in seen:
      return [seen[complement], i] #[value, index]
    # if complement is not in the seen hash table then we add num and its index i to sean and continue iterating
    seen[num] = i
  return [] # if we iterate through entire array and didnt find pair of numbers that add up to target
    
