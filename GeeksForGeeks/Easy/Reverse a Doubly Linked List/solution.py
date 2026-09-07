""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        prev = None
        current = head
        if head.next is None:
            return head
        while current is not None:
            nextNode = current.next
            current.next = prev
            current.prev = nextNode
            prev = current
            current = nextNode
        return prev
            
        