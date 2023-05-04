class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, you need to find one continuous subarray such that if you only sort
        this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.
        Return the shortest such subarray and outputs its length
        """
        n = len(nums)
        #left and right are the left and right boundaries of the unsorted subarray
        left, right = n, 0
        #stack is an empty list that will be used to keep track of indices of elements in the input array 'nums'
        stack = []
        
        for i in range(n): #iterates over the elements of the input array nums
            #for each element nums[i], checks whether the previous element at index stack[-1] is > nums[i]
            while stack and nums[stack[-1]] > nums[i]:
                #if it is, it updates the left boundary 'left' to be the minimum value of 'left' and the index
                #at the top of stack, and pops that index off the stack
                left = min(left, stack.pop())
                #this process continues until either the stack is empty or the previous element is not greater than nums[i]
                #than nums[i], after that it appends the current index 'i' to the stack.
            stack.append(i)

        
            #this loop effectively finds the left boundary of the unsorted subarray
            stack = []
            #this loop does the same as the previous loop but in reverse order
            #it iterates over nums elements in reverse
            for i in range(n - 1, -1, -1):
                #for each element jnums[i], it checks whether the next element at index stack[-1] is less than nums[i]
                while stack and nums[stack[-1]] < nums[i]]:
                    #if it is then it updates the right boundary to be the maximum value of right and the index
                    #at the top of the stack, and pops that index off the stack
                    #this process continues until either the stack is empty or the next element is less than nums[i]
                    right = max(right, stack.pop())
                    #after that it appends the current index i to the stack.
                    #this loop effectively finds the right boundary of the unsorted subarray
                stack.append(i)
                
            #this line calculates the length of the unsorted subarray by subtracting the left boundary from the right boundary
            #and adding 1 (to include both boundaries in the subarray). 
            return right - left + 1 if right > left else 0
            #if the right boundary is less than or equal to the left boundary, it returns 0 (indicating that the input array is already sorted).

