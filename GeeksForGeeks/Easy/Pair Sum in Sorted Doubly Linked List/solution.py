# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        right = head

        # Find tail
        while right.next:
            right = right.next

        left = head
        result = []

        while left != right and right is not None and right.next != left:

            total = left.data + right.data

            if total == target:
                result.append([left.data, right.data])
                left = left.next
                right = right.prev

            elif total < target:
                left = left.next

            else:
                right = right.prev

        return result