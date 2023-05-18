class Solution:
    """
    Given an array nums as input containing n distinct
    numbers in the range [0,n] return the only number
    in the range that is missing from the array
    """
    def missingNumber(self, nums: List[int]) -> int:
        # you can utilize the mathematical formula for the sum of consecutive integers
        n = len(nums)

        #expected_sum variable is calculated using the formula of the sum of consecutive integers from 0 to n
        expected_sum = n * (n+1) // 2

        #actual_sum variable is calculated by summing all of the elements in the nums array using the sum() function
        actual_sum = sum(nums)

        #finally the function returns the difference between the expected_sum and the actual_sum, which represents the missing number
        return expected_sum - actual_sum
