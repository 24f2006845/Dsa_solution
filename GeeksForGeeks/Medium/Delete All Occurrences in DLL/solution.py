# Structure of the doubly linked list Node 
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        current = head

        while current:
            if current.data == x:
                if current == head:
                    head = current.next
                    if head:
                        head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
            current = current.next
        return head
                
                