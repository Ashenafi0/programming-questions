# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head and head.next==None:
            return True
        elif head.next and head.next.next==None:
            return head.val==head.next.val
        prev=None
        curr=head
        slow=head
        fast= head
        while fast and fast.next:
            fast=fast.next.next
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
            
        if fast and fast.next==None:
            temp=prev
            slow=slow.next
            while temp or slow:
                if slow.val!=temp.val:
                    return False
                slow=slow.next
                temp=temp.next
        else:
            while prev or slow:
                if prev.val!=slow.val:
                    return False
                prev=prev.next
                slow=slow.next
        return True
        