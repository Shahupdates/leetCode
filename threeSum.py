"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i!= k, and j != k, and nums[i] + nums[j] = nums[k] == 0
Notice that the solution set must not contain duplicate triplets

This solution has a time complexity of O(n^3) because its not efficient for large input arrays, 
2-pointer approach is more efficient with O(n^2)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # Avoid duplicating result
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    # Found a triplet
                    res.append((nums[i], nums[l], nums[r]))
                    
                    # Skip duplicate numbers
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
        return res
