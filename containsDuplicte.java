/*
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct
*/

class Solution{
  
  public boolean containsDuplicate(int[] nums){
      // create a HashSet to store the unique elements encountered so far  
      Set<Integer> set = new HashSet<>();

      /*
      Iterate through array using a for-each loop, check each element to see if its
      already in the HashSet using the contains() method, if we have a duplicate element, return true;
      Else just add it to the HashSet and continue iterating
      O(n) time complexity and O(n) space complexity, n is the length of the input array nums
      */
      // iterate through the array nums
      for(int num : nums){
          // check if the elements already in the HashSEt
          if(set.contains(num)){
              return true;
          } else {
              //add the element to the HashSet
              set.add(num);
          }
      }
      //no duplicates so return false;
      return false;

  }
}
