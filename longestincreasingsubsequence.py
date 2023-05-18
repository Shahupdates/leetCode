class Solution:
    """
    Given an integer array nums
    return the length of the longest strictly 
    increasing
    subsequence
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        #checks if list is empty, if it is return 0
        if not nums:
            return 0
        
        n = len(nums)
        #dp list initialized with all elements set to 1, list stores the 
        #Longest increasing subsequence that end at each index
        dp = [1] * n
        #nested loops iterate over the array
        #outer loop iterates from the second element to the last, 
        #representing the current element we are considering
        for i in range(1, n):
            #inner loop iterates from the first element to the element before the current one
            for j in range(i):
            #it checks if the current element is > than previous element, 
                if nums[i] > nums[j]:
                    """
                    if it is then we can extend the increasing subsequence ending at the current index
                    updates the length of the LIS at index i if the condition is satisfied, 
                    takes the maximum between the current length at index i and the length at 
                    index j +1.
                    """
                    dp[i] = max(dp[i], dp[j]+1)

        #function returns the maximum value in the dp list
        #which represents the length of the longest strictly increasing subsequence
        return max(dp)
