''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # cycle detected

                count = 1
                current = slow.next

                while current != slow:
                    count += 1
                    current = current.next

                return count

        return 0
        