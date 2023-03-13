# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        res=[]
        while curr:
            res.append(curr.val)
            curr=curr.next
        dummy=ListNode()
        res.sort()
        l3=dummy
        while res:
            l3.next=ListNode(res.pop(0))
            l3=l3.next
        
        return dummy.next
            
        