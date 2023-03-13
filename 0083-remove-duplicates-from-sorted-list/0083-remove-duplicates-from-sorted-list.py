# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        slow=dummy
        fast=head
        while fast and fast.next:
            if fast.val==fast.next.val:
                slow.next=slow.next.next
                fast=fast.next
            else:
                slow=fast
                fast=fast.next
        
        return dummy.next
        