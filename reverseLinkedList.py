# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Given the head of a singly linked list as input, reverse the list, and return the reversed list.
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      """
      To reverse a singly linked list, you can use an iterative approach that involves reversing the pointers
      of the nodes.
      """
      prev = None #indicating the previous node in the reversed list
      curr = head #representing the current node being processed
      
      while curr: #iterates over the curr pointer reaches the end of the original list (curr would then become None..)
        next_node = curr.next #the next_node variable is assigned the value of curr.next to temporarily store the next node in the original list
        curr.next = prev  #the curr.next node pointer is then updated to point to the prev node, reversing the direction of the pointer.
        prev = curr #the prev variable is updated to the current node 
        curr = next_node #then curr variable is updated to the next node in the original list)
        
      #after the loop the prev variable points to the last node of the original list, which is now the head of the reversed list
      #finally the function returns prev which is the head of the reversed list
      return prev
