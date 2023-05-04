"""
Given an array of meeting time intervals where intervals[i] = [start_i, end_i]
Determine if a person could attend all meetings

To solve this problem, we need to check if any two intervals overlap. If they do,
then it would be impossible for a person to attend all of the meetings since they would
be attending two meetings at the same time.
One way to check for overlapping intervals is to sort the intervals based on their starting 
time. 
Then we can iterate through the sorted intervals and check if the current interval overlaps
with the previous one.
Because of the sorting step, the time complexity of this solution is O(n * log n). Space Complexity is O(1) 
since we are not using any extra data structures
"""
class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    """
    This is a python list method that sorts the elements of the intervals list 
    in ascending order based on the first element of each interval.
    The 'key' parameter specifies a function that takes an element of the list as input
    and returns a value to use for sorting. In this case, the 'lambda x: x[0]' function
    takes an interval x, and returns its first element x[0], which is the start time of the interval.
    """
    intervals.sort(key = lambda x: x[0])
    
    #check if any 2 consecutive intervals overlap
    for i in range(1, len(intervals)):
      # for each iteration we compare the start time of the current interval: intervals[i][0]
      # with the end time of the previous interval: intervals[i-1][1]
      # if the start time of the current interval is less than the end time of the previous interval, then the 
      # two meetings overlap, so we say its false.
      if intervals[i][0] < intervals[i-1][1]:
        return False
    
    #If we reach here, all intervals are non-overlapping.
    return True
