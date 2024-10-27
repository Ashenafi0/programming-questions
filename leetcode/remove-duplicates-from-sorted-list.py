# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy=ListNode(next=head)

        prev,cur=head,head.next
        while cur:
            if prev.val==cur.val:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
        return dummy.next
        