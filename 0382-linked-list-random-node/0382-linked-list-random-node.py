# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
            self.nodes_array = self.buildArray(head)
            self.n = len(self.nodes_array)
        
    def buildArray(self, head):
            nodes_array = list()
        
            ptr = head
            while ptr is not None:
                    nodes_array.append(ptr)
                    ptr = ptr.next
           
            return nodes_array
            
        
    def getRandom(self) -> int:
            i = random.randint(0, (self.n)-1)
            return self.nodes_array[i].val