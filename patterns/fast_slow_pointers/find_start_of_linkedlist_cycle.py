# !difficulty: medium

''' Problem:
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
'''

''' Solution:
If we know the length of the LinkedList cycle, we can find the start of the cycle through the following steps:
    1. Take two pointers: pointer1 and pointer2;
    2. Initialize both pointers to point to the start of the LinkedList;
    3. We need to find the length of the LinkedList cycle;
    4. Let’s assume that the length of the cycle is K nodes. Move pointer2 ahead by K nodes;
    5. Now, keep incrementing pointer1 and pointer2 until they both meet:
    6. As pointer2 is K nodes ahead of pointer1, which means, pointer2 must have completed one loop in the cycle when both pointers meet.
The meeting point will be the start of the cycle.
'''

# solution one
# Complexity:
# O(n) time - where n is the number of nodes in the linked list
# O(1) space
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution:
    def findCycleStart(self, head):
        cycleLength = 0
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cycleLength = self.calculateCycleLength(slow)
                break
        return self.findStart(head, cycleLength)

    def calculateCycleLength(self, slow):
        current = slow.next
        cycleLength = 1
        while current != slow:
            current = current.next
            cycleLength += 1        
        return cycleLength

    def findStart(self, head, cycleLength):
        pointer1, pointer2 = head, head
        for i in range(0, cycleLength):
            pointer2 = pointer2.next
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1