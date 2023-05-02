"""
Write a function that takes the binary representation of an unsigned integer and returns
the number of "1" bits it has 
"""

class Solution:
  def hammingWeight(self, n: int) -> int:
    count = 0
    #look while the input integer is not 0
    while n:
      count += n & 1 #check if the least significant bit (LSB) of the input integer is a "1" or not
      #if it is we increment the count variable then we right shift the input integer by one bit (divide it by 2)
      #to discard the LSB and repeat the process until the input integer becomes 0, then return count
      n >> 1
    return count

 
## easier way

def hammingWeight(self, n: int) -> int:
  #use the bin() function to convert the integer to its binary representation as a string, then we count 
  #the number of 1 characters in the binary string
  return bin(n).count('1')
  
