# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,None)
        dummy.next=head
        first=dummy
        for _ in range(n):
            first=first.next
        slow=dummy
        while first.next!=None:
            slow=slow.next
            first=first.next
        slow.next=slow.next.next
        return dummy.next
        


        
        