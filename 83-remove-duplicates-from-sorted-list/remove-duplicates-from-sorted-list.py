# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict={}
        curr=head
        l=[]
        while curr:
            if curr not in dict:
                dict[curr.val]=0
            else:
                dict[curr.val]=1
            curr=curr.next
        for i,c in dict.items():
            if c ==0 :
                l.append(i)
        dummy = ListNode(0)
        current = dummy
        
        for val in l:
            current.next = ListNode(val)
            current = current.next
        
        # Return the head of the newly formed linked list
        return dummy.next