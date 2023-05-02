"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times
Given the sorted rotated array nums of unique elements, return the minimum element of this array
Algorithm must be O(log n) time
Example: nums = [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2] if it was rotated 4 times
"""

class Solution:
  """
  Use binary search, since the array is sorted we can compare the middle element
  of the array with the 1st and Last elements to determine which half of the array
  is sorted.
  If the middle element is > than the first element, then the left half of the array is sorted
  and the minimum element must be in the right half, otherwise the right half of the array
  is sorted and the minimum element must be in the left half. We can then repeat the process
  on the appropriate half of the array until we find the minimum element
  This algorithm has a time complexity of O(log n) since we use binary search to reduce the search
  space by half at each iteration.
  """
  def findMin(self, nums: List[int]) -> int:
    #we initialize two pointers, left and right to the first and last indices of the array
    left = 0 
    right = len(nums) - 1
    #we use a while loop to repeat the binary search process until left and right are equal
    #which means we have found the minimum element.
    while left < right:
      #calcuate the middle index mid using integer division
      mid = (left+right) // 2
      #we then compare nums[mid] with nums[right] to determine which half of the arry is sorted
      if nums[mid] > nums[right]:
        #if nums[mid] > nums[right] then the right half of the array is sorted and has the minimum element
        #therefore we update left to mid + 1 to search the right half of the array.
        left = mid + 1
      else:
        #otherwise  if nums[mid] < nums[right] then the left half of the array is sorted and the 
        #minimum element must be in the left half, therefore we update right to mid to search left half
        right = mid
        #we repeat the process until left and right are equal, and then we return the element
        #at index left, which is the minimum element in the array.
    return nums[left]
    
