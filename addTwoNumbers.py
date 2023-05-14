# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given two non-empty linked lists representing two non-negative integers
            Digits are stored in reverse order, and each of their nodes contain a single digit
            1. Add the two numbers and return the sum as a linked list
        """

        # a dummy node is created as the head of the result linked list to simplify the logic
        dummy = ListNode(0)
        #current is a reference to the current node in the result linked list, it starts with the dummy node
        curr = dummy
        #this variable keeps track of the carry value while adding the corresponding digits from "l1" and "l2"
        carry = 0
        
        #continues until there are no more nodes in both l1 and l2, and there is no remaining carry
        while l1 or l2 or carry:
            #inside the loop the values of l1 and l2, and the carry, are added together the carry is then updated with the sum value, and the respective nodes are moved forward.
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            #a new node is created wtih the value carry % 10, this value represents the digit at the current position in the resulting linked list, this calculates the remainder when carry is divided by 10, if carry and the sum of l1 and l2's corresponding digits is 14, the remainder of 14 divided by 10 is 4. Therefore a new node with the value 4 is created and assigned to curr.next, this digit will be apart of the resulting linked list
            curr.next = ListNode (carry % 10)
            #the curr node is moved to the next position, aka updated to point to the newly created node, this ensures that the next iteration of the while loop adds nodes to the correct position in the resulting linked list
            curr = curr.next
            #the carry value is updated by performing an integer divison by 10
            carry //= 10
        #the result linked list is returned by skipping the dummy node (returning dummy.next)
        return dummy.next
