"""
You are given an array of strings tokens that represents an arithmetic expression in a reverse polish notation
Evaluate the expression. Return an integer that represents the value of the expression.
Valid operators: + , - , *, and /
Each opreand may be an integer or another expression
The division between two integers always truncates towards 0
There will not be any division b yzero
The input represents a valid arithmetic expression in a reserve polish notation
The answer and all the intermediate calculations can be represented in a 32-bit integer
"""

class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    #stack data structure to hold operands and perform operations in the correct order. 
    #iterates through the tokens and checks if a token is an operator or an operand
    stack = [] 
    
    for token in tokens:
      if token in {'+', '-', '*', '/'}:
        b, a = stack.pop(), stack.pop()
        #if its an operator, it pops the last two operands from the stack, performs the operation
        #and pushes the result back onto the stack, if its an operand it pushes the integer value of the token
        #onto the stack
        if token == '+':
          stack.append(a+b)
        elif token == '-':
          stack.append(a-b)
        elif token == '*':
          stack.append(a*b)
        elif token == '/':
          stack.append(int(a/b))
      else:
        stack.append(int(token))
    
    #the function returns the value at the top of the stack, which is the result of the arithmetic expression
    return stack[0]
