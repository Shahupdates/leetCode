/*
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
*/

class Solution {
    public boolean canJump(int[] nums) {

       // farthest index we can reach from the first index
       int farthest = 0;
       
       // loop through the array, updating farthest at every step
       for(int i = 0; i < nums.length; i++){
           // if at any point farthest is less current index return false
           if(farthest < i){
               return false;
           }
           // otherwise update farthest with the formula
           // that calculates the farthest index to go from current index
           farthest = Math.max(farthest, i + nums[i]);
       }
       // if we haven't returned false yet, we've reached the end.
       return true;        
    }
}

/*
To solve this problem, we can use a greedy approach. We start at the first index and keep track of the farthest index we can reach from the current index. We keep updating this farthest index as we move forward in the array. If at any point, the farthest index is less than the current index, then we cannot reach the last index, and we return false.
*/
