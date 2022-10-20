# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        z=dummy
        curr=head
        while curr:
            temp=curr.next
            if curr.val==val:
                z.next=temp
            else:
                z=curr
            curr=curr.next
        
        return dummy.next
            
            
        