class Solution:
  """
  You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
  Return true if you can reach the last index, or false otherwise.
  """
    def canJump(self, nums: List[int]) -> bool:
    """
    To solve this problem, you can use a greedy approach where you maintain a variable "max_reach" 
    that represents the furthest index you can reach from the current position. At each index 'i', you
    update max_reach to be the maximum of max_reach and 'i + nums[i]. If max_reach is >= the last index,
    you can reach the end of the array and you return True.
    Otherwise you continue iterating through the array until max_reach is less than the current index,
    in which case you can no longer reach the current end and you return "False"
    """
        max_reach = 0
        for i in range(nums.length):
          if i > max_reach:
            return False
          max_reach = max(max_reach, i + nums[i])
          if max_reach >= len(nums) - 1:
            return True
        return False
  
