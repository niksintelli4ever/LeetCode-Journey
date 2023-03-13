# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev=None
        dummy=ListNode(0,head)
        slow=dummy
        fast=dummy
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
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        
        return True
        