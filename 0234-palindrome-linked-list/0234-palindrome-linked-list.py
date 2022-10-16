# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=ListNode(0,head)
        curr=head
        fast=head
        prev=None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=prev
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        second=prev
        while head and second:
            if head.val!=second.val:
                return False
            head=head.next
            second=second.next
        return True
            
        