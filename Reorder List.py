# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return head
        
        start = head
        end = head
        
        while end.next.next !=None:
            end = end.next.next
            if end.next == None :
                break
            start = start.next
        
        head2 = start.next
        start.next = None
        
        prev = None
        
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp   
        
        current = head
        while current.next!=None:
            temp = current.next
            current.next = prev
            current = prev
            prev = temp
            
        if prev != None:
            current.next = prev