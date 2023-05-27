"""
Find minimum in a rotated sorted array
Given an input array of length n sorted in ascending order but it can rotated between 1 and n times
Take rightmost element and move it to beginning is rotating by 1, rotating it by 2 is taking last 2 elements and move it to the beginninng.
Find the minimum element of the array
Every value in the array is unique
Algorithm has to be O(log n), it can't be iterated directly.
Binary search would work but not a traditional binary search
Binary search has left and right pointer, if we get to a point where the entire array is sorted we can just return the left value.
Left pointer initialized to first on left, right pointer initialized to first on right
*Find the position where the elements are not in increasing order: [3, 4, 5, 1, 2] , 5,1 is the pivot
Take half of left and right the middle pointer is 5 in [3,4,5,1,2]
Result is 5.
Now the question is are we gonna search the left or the right, where are we gonna find a value smaller than 5, since we rotated the array,
we have 2 portions of the array that are sorted.
With 5, are we currently in the left sorted portion or the right sorted portion
If we rotated the array the left array will always have the larger values than the right side.
If our middle pointer is a value in the left sorted portion, then we search the right sorted portion.
Every value in the right sorted portion is going to be smaller than the left.
We check if the current middle: 'm' value is is greater than or equal to the left most value, which means its apart of the left
sorted portion: nums[m] >= nums[L], so we want to search the right.
We want to find even smaller values than 'm'.
If our middle pointer 'm' is >= L: in this case: [3,4,5,1,2] , is 5 >= 3, Yes
If this is false, lets say if our m was '1', then we would want to search the left.
nums[m] >= nums[L] # 5>= 3? No, so cross out [3,4,5], we have [1,2], shift Left pointer to [1,2], this portion of the array is already
in sorted order, left most value is the minimum. So return 1.
  search Right  
 else:
  search Left
  
If middle pointer is 1 in [3,4,5,1,2] . Initial result is 1.
Is middle value >= nums[L] ? No, so we go to the else case and search left, cross out [1,2], so we have [3,4,5], our Right pointer
is now 5, Range is sorted now, so we return the leftmost value. 
3 is not smaller than my result, so our result stays the same and we don't have to search this entire portion because its already sorted.
"""

class Solution:
   def findMin(self, nums: List[int]) -> int:
   res = nums[0]
   l,r = 0, len(nums) - 1
   
   while l <= r:  #keep running our binary search while our left pointer is less than our right
    if nums[l] < nums[r]:
      res = min(res, nums[l])
      break
    
    m = (l + r) // 2
    res = min(res, nums[m]
    if nums[m] >= nums[L]:
      l = m + 1 #cross out 
    else:
      r = m - 1
   return res
    
   
    
