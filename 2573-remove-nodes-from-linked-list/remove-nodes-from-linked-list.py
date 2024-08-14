# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list first
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Now remove nodes that are less than the max seen so far
        max_val = float('-inf')
        new_head = prev
        curr = prev
        prev = None
        
        while curr:
            if curr.val >= max_val:
                max_val = curr.val
                prev = curr
            else:
                if prev:
                    prev.next = curr.next
            curr = curr.next
        
        # Reverse the list back to its original order
        head = None
        while new_head:
            next_node = new_head.next
            new_head.next = head
            head = new_head
            new_head = next_node
        return head
