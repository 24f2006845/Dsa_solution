# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
## solution 1 using two pass 
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

## solution 2  by one pass 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
# both have same complexity just i write solution2 bcz leetcode says that
        
        
