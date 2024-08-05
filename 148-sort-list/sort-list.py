# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ele=[]
        curr=head
        while curr:
            ele.append(curr.val)
            curr=curr.next
        ele.sort()
        sorted_head=ListNode(ele[0])
        curr=sorted_head
        for i in ele[1:]:
            curr.next=new_node=ListNode(i)
            curr=curr.next
        return sorted_head