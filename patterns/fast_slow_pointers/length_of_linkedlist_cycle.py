# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dda065488110f74a930ebc

''' Problem:
Given the head of a LinkedList with a cycle, find the length of the cycle.
'''

# solution two
# Complexity:
# O(n) time - where n is the number of nodes in the LinkedList
# O(1) space
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution:
    def findCycleLength(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            # Check if the slow and fast pointers meet, indicating the presence of a cycle
            if slow == fast:
                return self.calculate_cycle_length(slow)
        return 0

    def calculate_cycle_length(self, slow):
        current = slow.next
        cycle_length = 1

        # Count the length of the cycle by moving through it until we reach the starting point again,
        # where the starting point is indicated by the slow pointer
        while current != slow:
            current = current.next
            cycle_length += 1        
        return cycle_length

# solution two
# Complexity:
# O(n) time - where n is the number of nodes in the LinkedList
# O(1) space
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution:
    def findCycleLength(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            # Check if the slow and fast pointers meet, indicating the presence of a cycle
            if slow == fast:
                return self.calculate_cycle_length(slow)
        return 0

    def calculate_cycle_length(self, slow):
        current = slow
        cycle_length = 0

        # Count the length of the cycle by moving through it until we reach the starting point again,
        # where the starting point is indicated by the slow pointer
        while True:
            current = current.next
            cycle_length += 1        
            if current == slow:
                break
        return cycle_length
