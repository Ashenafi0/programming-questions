# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head and head.next==None or head==None:
            return head
        p1=None
        p2=head
        p3=None
        while p2 :
            p3=p2.next
            p2.next=p1
            p1=p2
            p2=p3
        return p1


        