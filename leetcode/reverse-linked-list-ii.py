# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left==right:
            return head
        dummy=ListNode()
        dummy.next=head

        cur=dummy
        prev=None
        for i in range(left):
            prev=cur
            cur=cur.next
        lef=cur

        nex=cur.next
        temp=None
        for i in range(left,right):
            temp=nex.next
            nex.next=cur
            cur=nex
            nex=temp
        prev.next=cur
        lef.next=temp
        return dummy.next
          






        