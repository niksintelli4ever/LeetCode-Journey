# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return 
        while len(lists)>1:
            res=[]
            for i in range(0,len(lists),2):
                list1=lists[i]
                list2=lists[i+1] if i+1<len(lists) else 0
                res.append(self.mergeTwo(list1,list2))
            lists=res
        return lists[0]
    
    def mergeTwo(self,l1,l2):
        l3=ListNode()
        dummy=l3
        while l1 and l2:
            if l1.val<=l2.val:
                l3.next=l1
                l1=l1.next
            else:
                l3.next=l2
                l2=l2.next
            l3=l3.next
        
        if l1:
            l3.next=l1
        if l2:
            l3.next=l2
        
        return dummy.next
        