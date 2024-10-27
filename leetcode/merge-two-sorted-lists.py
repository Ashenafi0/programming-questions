# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tem=dummy
        def custom(node1,node2,temp):
            if node1==None:
                temp.next=node2
                return
            if node2==None:
                temp.next=node1
                return 
            if node1.val<=node2.val:
                temp.next=node1
                custom(node1.next,node2,temp.next)
            else:
                temp.next=node2
                custom(node1,node2.next,temp.next)
            return temp
        custom(list1,list2,tem)
        return dummy.next





        