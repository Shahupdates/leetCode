"""
There is an integer value nums sorted in ascending order (with distinct values)
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index
k such that the resulting array is (0-indexed). For example: [0,1,2,4,5,6,7] might be rotated
at pivot 3 and become [4,5,6,7,0,1,2]. 

Given the array nums after the possible rotation and an integer target, return the index
of target if it is in nums or -1 if it is not in nums.
"""

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    #we repeat binary search process until left > right, means that we have
    #exhausted the search range and the target is not in the array
    while left <= right:  
      #calculate middle index mid using integer divison
      mid = (left+right) // 2
      #we then compare nums[mid] with the first and last elements of the array to determine
      #which half of the array is sorted. 
      if nums[mid] == target:
        return mid
      elif nums[mid] >= nums[left]:
      #If nums[mid] >= nums[left] then the left half of the array is sorted. 
      #We check if the target is within the range of the left half, from
      #nums[left] to nums[mid] by comparing target with nums[left] and nums[mid]
        if target >= nums[left] and target < nums[mid]:
          #if the target is within the range we update right to mid - 1 to search the left half
          #of the array, otherwise we update left to mid + 1 to search the right half of the array
          right = mid - 1
        else:
          left = mid + 1
      else:
        #if nums[mid] < nums[left] then the right half of the array is sorted, we check
        #if the target is within the range of the right half, from nums[mid] to nums[right]
        if target > nums[mid] and target <= nums[right]:
          #we update left to mid + 1 to search the right half of the array otherwise
          #we update right to mid - 1 to search the left half of the array.
          #we repeat the process until we either find the target or exhaust the search range
          left = mid + 1
        else:
          right = mid - 1
          #if we find the target we return its index as in line 3, otherwise we return -1
          #to indicate that the target is not in the array, O(n log n) algorithm because
          #we use binary search to reduce the search space by half at each iteration.
    return -1;
      
      
