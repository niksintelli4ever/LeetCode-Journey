# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy=ListNode(0,head)
        slow=dummy
        fast=dummy
        prev=None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        first=head
        second=prev
        while first and second:
            temp1,temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2
        
        return dummy.next
            
            
        