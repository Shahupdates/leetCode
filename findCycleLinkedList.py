# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Given head, the head of a linked list, determine
    if the linked list has a cycle in it
    There is a cycle in a linked list if there is some
    node in the list that can be reached again 
    by continuously following the next pointer.
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to, pos is not passed as a parameter

    hasCycle takes the head of a linked list as input and
    returns true if there is a cycle in the linked list, otherwise return false
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Use Floyd's cycle finding algorithm 
        
        #condition checks if the linked list has fewer than 2 nodes, which means no cycles
        if not head or not head.next:
            return False


        slow = head     #initialized with the head
        fast = head.next    #initialized with the next node of the head

        #while loop continues as long as the slow and fast pointers do not meet
        while slow != fast:
            #this condition checks if the fast pointer or its next pointer is None
            if not fast or not fast.next:   
                #if either of them is None, it means that the end of the linked lists been reached
                #and that there is no cycle, so return False to indicate the absence of a cycle
                return False
            #inside the loop the slow pointer moves one step forward
            slow = slow.next
            #inside the loop the fast pointer moves two steps forward
            fast = fast.next.next
            #the movement of the pointers simulate the tortoise and hare chasing scenario,
            #if there is a cycle, the fast pointer will eventually catch up with the slow pointer
            #and they will meet, if there is no cycle the fast pointer will reach the end of the
            #linked list before it can catch up with the slow pointer

        #once the loop exits, if the slow and fast pointes have met (slow==fast)
        #it indicates a cycle in the linked list and so it returns true
        return True
