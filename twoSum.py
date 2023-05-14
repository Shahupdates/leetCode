class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        /*
        twoSum aims to find two numbers in a list that ends up to a given target value
        This pattern optimizes the search process by trading space complexity for time complexity, by storing previously seen numbers and their indices in a hash table, you can check if the complement exists in constant time so the complexity is reduced from O(n^2) (nested loop approach) to O(n) (single loop approach)
        Classic example of using a hash table to efficiently solve a problem that involves finding pairs of elements with a specific property (in this case adding up to a target value)
        */
        #initializes an empty dictionary named seen to keep track of previously seen numbers and their indices
        seen = {}
        #loop iterates over the elements of the nums list (num) along with their indices (i)
        for i, num in enumerate(nums):
            #the varialbe complement is calculated as the difference between the target value and the current number
            #example if the value at index 0 is 9, and the target=10 then the complement would be 10-9 which is 1
            complement = target - num
            #checks if the complement is already present in the seen dictionary, if it is that means we have found a pair of numbers that add up to the target
            if complement in seen:
                #in that case, the function returns the index's of the complement and the current number as a list [seen[complement], i]
                return [seen[complement], i]
            #if the complement is not in the seen dictionary, it means we haven't encountered the number that pairs with the current number yet. So we add the current number to the seen dictionary (it would be the key) and with its index (it would be the value)
            seen[num] = i
        #if the loop finishes without finding a solution, the function returns an empty list indicating there are no 2 numbers that add up to the target value
        return []
