"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
using all the original letters exactly once

Solution:
To solve this problem, we use a dictionary to keep track of the frequency of each character in the string s, 
then we iterate through the string t, and decrement the frequency of each character in the dictionary.
If at any point, the frequency of a character becomes negative, or a character t is not in the dictionary
then t is not an anagram of s. If we reach the end of t, without any issues, then t is an anagram of s.
"""
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    
    freq = {} #dictionary
    for char in s:
      # this line of code is updating the frequency count of each character in the string s
      # freq.get(char, 0) returns the current count of char in the freq dictionary, if the char is not in
      # the current freq dictionary then it returns the default value of 0
      # we add 1 to the count returned by freq.get(char, 0), which increments the count of char
      # finally we assign the updated count to the key char.
      freq[char] = freq.get(char, 0) + 1
      
     for char in t:
      if char not in freq or freq[char] == 0: # if the character is not in the dictionary or has a freq of 0
        return False
      freq[char] -= 1 #if each char is in the dictionary w/ a positive frequency, we decrement that character by 1
      
     return True # if we reached the end without any issues, then t is an anagram of s, and we return True
