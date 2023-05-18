# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Given the head of a singly linked list as input, reverse the list, and return the reversed list.
    This code aims to reverse a singly linked list by changing the direction of the pointers between nodes
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      """
      To reverse a singly linked list, you can use an iterative approach that involves reversing the pointers
      of the nodes.
      """
      prev = None #indicating the previous node in the reversed list
      curr = head #representing the current node being processed

      #iterates over the curr pointer reaches the end of the original list (curr would then become None..)
      while curr: 
      
        #the next_node variable is assigned the value of curr.next to temporarily store the 
        #next node in the original list before modifiyng the pointer
        next_node = curr.next 

        #the curr.next node pointer is then updated to point to the prev node, this reverses the direction of the pointer
        #connecting the current node to the previous node
        curr.next = prev  
        
        #the prev variable is updated to the current node as it will be the previous node in the next iteration
        prev = curr 
        
        #then curr variable is updated to the next node which allows the loop to progress to the next node in the original list
        curr = next_node 
      
      #once the loop finishes, the prev variable will point to the last node of the original list, which is now the head of the reversed list

      #finally the prev node is returned, representing the head of the reversed list
      return prev
