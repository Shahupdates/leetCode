class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """
        Given an array of integers arr, sort the array by performing a series of pancake flips.
        In one pancake flip, we do the following steps:
            Choose an integer k where k >= 1, and k <= arr.length
            Reverse the sub-array arr[0,..., k-1] 
        For example if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3,
        we reverse the sub array [3,2,1], so arr = [1,2,3,4] after the pancake flip.
        Return an array of the k values corresponding to a sequence of pancake flips that sort arr.
        #Any valid answer that sorts the array within 10 * arr.length flips = correct
        """
        n = len(arr)
        res = []
        for i in range (n, 1, -1):
            #find the index of the maximum element in the first i elements
            max_index = arr.index(max(arr[:i]))
            
            if max_index == i - 1:
                #if the max element is already at the end, skip this interaction
                continue
            elif max_index == 0:
                #if the max element is at the beginning, flip the entire array
                arr[:i] = arr[:i][::-1]
                res.append(i)
            else:
            #otherwise flip the subarray to bring the maximum element to the 
            #beginning and then flip the entire subarray to bring it to the end.
            arr[:max_index+1] = arr[:max_index+1][::-1]
            res.append(max_index+1)
            arr[:i] = arr[:i][::-1]
            res.append(i)
    
        return res
        
