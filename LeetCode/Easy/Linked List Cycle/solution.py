# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        visited = []
        while current is not None:
            if current in visited:
                return True
            visited.append(current)
            current = current.next
        return False

        