
class Solution:
  """
  Write a function that takes the binary representation
  of an unsigned integer 'n' and returns the number of '1' bits it has in its binary representation
  (also known as the Hamming weight)

  """
  def hammingWeight(self, n: int) -> int:
    #use the bin() function to convert the integer to its binary representation as a string
    #the resulting binary string includes a prefix of '0b' so we slice it starting from index 2 [2:] to remove the prefix
    binary_string = bin(n)[2:]
    #initialize the count variable to 0 representing the number of 1 bits
    count = 0
    for char in binary_string:
      #if the character is equal to 1 it means a 1 bit is encountered, so increment the count by 1
      if char == '1':
        count += 1
    #after the loop, the count represents the number of 1 bits in the binary representation of the input integer
    return count
