# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        flag=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                flag=1
                break
        if flag==0:
            return None
        
        slow2=head
        while slow and slow2:
            if slow==slow2:
                return slow
            slow=slow.next
            slow2=slow2.next
        
        
            
        