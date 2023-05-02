"""
A phrase is a palindrome, if after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Given a string s, return true if it is a palindrome, or false otherwise
"""

class Solution:
  def isPalindrome(self, s: str) -> bool:
    s = s.lower() #convert the string s to lowercase
    #remove all non-alphanumeric characters from the string using isalnum
    new_s = ''
    for char in s: 
      if char.isalnum(): #if the char is alphanumeric then append to new string new_s
        new_s += char
    # check if the resulting string is equal to its reverse by using the [::-1] slicing syntax to
    # reverse the string, if the reversed string is equal to the original then return true, otherwise return false
    return new_s == new_s[::-1]
        
