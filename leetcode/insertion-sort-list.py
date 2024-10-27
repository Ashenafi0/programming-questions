class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        sorted_list = ListNode()
        while head:
            current = sorted_list
            while current.next and current.next.val < head.val:
                current = current.next
            temp = head.next
            head.next = current.next
            current.next = head
            head = temp
        return sorted_list.next
