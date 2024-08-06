# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639105492e1c0a1cfe6c1eb9

''' Problem:
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
'''

# solution one
# Complexity:
# O(n) time - where n is the number of nodes in the LinkedList.
# As concluded in the README.md, once the slow pointer enters the cycle, the fast pointer will meet the slow pointer in the same loop.
# O(1) space
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
