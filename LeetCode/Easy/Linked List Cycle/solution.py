# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# solution 1
# brute force
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         current = head
#         visited = []
#         while current is not None:
#             if current in visited:
#                 return True
#             visited.append(current)
#             current = current.next
#         return False
# Floyd algo also called slow and fast pointer
 class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast :
                return True
        return False
        
