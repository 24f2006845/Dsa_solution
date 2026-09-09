# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        current = headRef
        prev = None

        while current is not None:
            if prev is not None and current.data == prev.data:
                prev.next = current.next

                if current.next is not None:
                    current.next.prev = prev
            else:
                prev = current

            current = current.next

        return headRef