# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head and head.next==None or head==None:
            return head
        greater_or_equal=ListNode()
        less_than=ListNode()
        less=less_than
        greater=greater_or_equal
        while head:
            if head.val<x:
                less.next=head
                less=less.next
            else:
                greater.next=head
                greater=greater.next
            head=head.next
        
            
            
        less.next=greater_or_equal.next
        greater.next=None

        return less_than.next    