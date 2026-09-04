# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head 
        prev = None
        length = 0
        while current is not None:
            length+=1
            current = current.next
        indexToDelete = length - n
        current = head
        count = 0
        if indexToDelete == 0:
            head = head.next
            return head
        while current is not None and count < indexToDelete :
            count +=1
            prev = current
            current = current.next
        prev.next = current.next
        return head
        
        