# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Initialize result as 0
        result = 0
        curr = head
        
        # Traverse the linked list
        while curr:
            # Shift the result to the left (multiply by 2) and add the current value
            result = result * 2 + curr.val
            # Move to the next node
            curr = curr.next
        
        return result