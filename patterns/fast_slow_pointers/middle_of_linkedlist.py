# !difficulty: easy

''' Problem:
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4
'''

# solution one: a bit cleaner
# Complexity:
# O(n) time - n is the number of nodes in the linked list
# O(1) space
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution:
    def findMiddle(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

# solution two
# Complexity:
# O(n) time - n is the number of nodes in the linked list
# O(1) space
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution:
    def findMiddle(self, head):
        slow, fast = head, head
        length = 1
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            length += 2
        if length % 2 == 0:
            return slow.next
        return slow
