# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        seen=set()
        temp_a=headA
        while temp_a:
            seen.add(temp_a)
            temp_a=temp_a.next
        temp_b=headB
        while temp_b:
            if temp_b in seen:
                return temp_b
            temp_b=temp_b.next
        return 
    
        