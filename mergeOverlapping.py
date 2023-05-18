class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Check if the intervals list is empty, if it is, return an empty list
        # because there are no intervals to merge
        if not intervals:
            return []

        # Sort the intervals based on their start times
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]  # Initialize merged with the first interval

        # Iterate over the remaining intervals
        for interval in intervals[1:]:
            # If the current interval overlaps with the last merged interval
            if interval[0] <= merged[-1][1]:
                # Update the end time of the last merged interval if needed
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                # If there is no overlap, append the current interval to merged
                merged.append(interval)

        # Return the merged list containing non-overlapping intervals
        return merged
