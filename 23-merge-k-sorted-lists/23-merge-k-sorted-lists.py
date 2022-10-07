# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        while len(lists)>1:
            res=[]
            for i in range(0,len(lists),2):
                list1=lists[i]
                list2=lists[i+1] if i+1 < len(lists) else None
                res.append(self.mergeTwo(list1,list2))
            lists=res
        return lists[0]  
    
    def mergeTwo(self,l1,l2):
        dummy=ListNode(0)
        curr=dummy
        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        if l1:
            curr.next=l1
            l1=l1.next
        if l2:
            curr.next=l2
            l2=l2.next
        
        return dummy.next
        
            
        