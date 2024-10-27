# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next==None or not head:
            return head

        odd_head=head
        even_head=head.next

        temp_odd=odd_head
        temp_even=even_head
        while temp_even and temp_even.next:
            temp_odd.next=temp_even.next
            temp_odd=temp_odd.next
            temp_even.next=temp_odd.next
            temp_even=temp_even.next
        temp_odd.next=even_head
        
        return odd_head



        