"""
Given an array of strings strs, group the anagrams together, you can return the answer in any order.

Solution: We initialize an empty dictionary anagram_groups to store the anagram groups.
The keys of the dictionary are the sorted strings
The values of the dictionary are the lists of strings that are anagrams of each other.
"""
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_groups = {}
    for string in strs: # we iterte through each string in the input list strs
    # for each string we sort its characters and join them back together to create a new string
      sorted_string = ''.join(sorted(string))
      #if the input string is cat, then the sorted string will be act
      #we check if the sorted_string is already in the dictionary we created
      if sorted_string in anagram_groups:
        #if it is then we append the current string to the list of anagrams corresponding to the sorted string
        anagram_groups[sorted_string].append(string) 
      else:
        #if it is not then we create a new list with the current list as its only element
        #and add it to anagram_groups with the sorted_string as its key
        anagram_groups[sorted_string] = [string]
    
    #once we have processed all the strings in strs, we return the list of anagrams, by calling the 
    # values() method of the anagram_groups dictionary and converting it to a list
    # the output of the groupAnagrams function is a list of lists, where each inner list contains strings
    # that are anagrams of each other
    return list(anagram_groups.values())
