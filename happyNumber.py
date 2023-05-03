"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the square of its digits
Repeat the process until the number equals 1(where it will stay) or it loops
endlessly in a cycle, which does not include 1.
Those numbers for which the process ends in 1 are happy.
"""

class Solution:
  """
  1. Create an empty set called seen
  2. While n is not 1
    a. convert n to a string and split it into a list of digits
    b. compute the sum of the square of each digit
    c. if the sum equals 1 return true
    d. if the sum is in seen return false
    e. otherwise add the sum to seen and set n to the sum.
  3. return True (we reached 1)
  """
  def isHappy(self, n:int) -> bool:
    seen = set()  #keep track of the numbers wev'e seen
    while n != 1:
      digits = []
      while n > 0:
        #this line of code converts an integer n into a list of digits
        #where each digit is an integer
        #str(n) converts the interger n into a string representation
        #[int(d) for d in str(n)] is a list comprehension that creates
        #a new list by iterating over each character d in the string
        #representation of n, and converting it to an integer using int(d)
        #for example if n is 123, then it creates the list [1,2,3]
        digits = [int(d) for d in str(n)]
        square_sum = 0
        for digit in digits:
          square_sum += digit ** 2
          #we repeatedly extract the digits of n, compute their squares
          #and sum them up until we reach either the number 1 (true)
          #or a number that we've already seen (false)
        n = square_sum
        if n in seen:
          return False
        seen.add(n)
     return True
  
  #faster implementation
  
class Solution:
  """
  Uses Floyds cycle finding algorithm to detect cycles
  in the sum of squares sequence and terminates early
  if a cycle is detected, which can improve the efficiency
  of the algorithm, especially for large inputs
  """
  def isHappy(self, n:[int]) -> bool:
    """
    slow moves 1 step at a time and fast moves 2 steps at a time
    if slow and fast ever point to the same number, weve detected
    a cycle and we can return false immediately. if we reach number 1, return true
    using this algorithm we can reduce the # of iterations needed to determine
    if a number is happy, especially for large input      
    """
    slow = fast = n #two pointers to iterate through the sequence of sum of squares
    #loop construct that creates n infinite loop
    #it is a way to execute a block of code repeatedly without specifying a specific condition
    #to exit the loop, once we detect a cycle, we can break out of the loop using the break
    #statement, if we reach 1, we can exit with returning True;
    while True:
      slow = self.sum_of_squares(slow)
      fast = self.sum_of_squares(self.sum_of_squares(fast))
      if slow == fast:
        break
    return slow == 1
  
  def sum_of_squares(self, n: [int]) -> int:
    square_sum = 0
    while n > 0:
      digit = n % 10  #returns the remainder when n is divided by 10, it gives us the last digit of the number n 
      square_sum += digit ** 2
      n //= 10 
      #returns n without the last digit after weve extracted it using n % 10
      #allows us to repeat the process with the remaining digits
      #until we've computed the sum of squares of all the digits
    return square_sum
