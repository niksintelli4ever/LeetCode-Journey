# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        linkedlist=[]
        while head:
            linkedlist.append(head.val)
            head=head.next

        def dfs(linkedlist):
            if not linkedlist:
                return
            mid=len(linkedlist)//2
            root=TreeNode(linkedlist[mid])
            root.left=dfs(linkedlist[:mid])
            root.right=dfs(linkedlist[mid+1:])
            return root
        return dfs(linkedlist)
        