# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        tortoise = head
        hare = head
        found = False
        
        if hare == None:
            return None
        
        while hare.next!=None and hare.next.next!= None:
            tortoise= tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                found = True
                break
                
        if not found:
            return None
        
        hare = head
        
        while tortoise!=hare:
            tortoise= tortoise.next
            hare = hare.next
            
        return tortoise