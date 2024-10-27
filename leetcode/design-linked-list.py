class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=Node(0)
        self.n=0
       
    
        

    def get(self, index: int) -> int:
       
        if index >self.n or self.head.next==None:
            return -1
        curr=self.head.next
        curr_indx=0
        while curr:
            if curr_indx==index:
                return curr.val
            curr=curr.next
            curr_indx+=1
        return -1
       
        

    def addAtHead(self, val: int) -> None:
        if self.head.next==None:
            self.head.next=Node(val)
            self.n+=1
        else:
            temp=Node(val)
            temp.next=self.head.next
            self.head.next=temp
            self.n+=1
       

        

    def addAtTail(self, val: int) -> None:
        curr=self.head
        
        while curr.next!=None:
            curr=curr.next
        curr.next=Node(val)
        self.n+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr=self.head.next
        temp_indx=0
        prev=self.head
        while curr and index!=temp_indx:
            prev=curr
            temp_indx+=1
            curr=curr.next
        if index==temp_indx or curr :
            temp=Node(val)
            prev.next=temp
            temp.next=curr
            self.n+=1
        
       

        
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.n:
            return
    
        prev = self.head
        curr = self.head.next
        temp_index = 0
    
        if index == 0:
            self.head.next = curr.next
            curr.next = None
            self.n -= 1
            return
    
        while curr and temp_index != index:
            temp_index += 1
            prev = curr
            curr = curr.next
        
        if curr and temp_index == index:
            prev.next = curr.next
            curr.next = None
            self.n -= 1

        


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)