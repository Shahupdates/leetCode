"""
Given a string s, containing just the characters (, ), {, }, [, and ]
determine if the input string is valid
An input string is valid if: open brackets must be closed by same type of brackets
Open brackets must be closed in the correct order
Every close bracket has a corresponding open brackets of the same type
"""

class Solution:
  def isValid(self, s: str) -> bool:
    stack = [] #use stack data structure to keep track of the opening brackets seen so far
    mapping = {")" : "(", "}" : "{", "]" : "["} #(key, value)
    for char in s: # iterate through the input string and check for each char if its an opening bracket
      if char in mapping.values():
        stack.append(char) #if it is we push it onto the stack
      elif char in mapping.keys(): #else if its a closing bracket we check if it matches the top element from the stack
        #if it matches the top element of the stack we pop the top element from the stac
        if not stack or mapping[char] != stack.pop():
           return False
        # if it doesnt match teh top element of the stack, we return false
      else:
        return False
    return not stack #if we iterated through the entire string and the stack is empty, we return true
