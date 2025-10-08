# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/remove-nth-node-from-end-of-list-medium

'''Problem:
Given a linked list, remove the last nth node from the end of the list and return the head of the modified list.

Input: list = 1 -> 2 -> 3 -> 4 -> 5, n = 2
Output: 1 -> 2 -> 3 -> 5
Explanation: The 2nd node from the end is "4", so after removing it, the list becomes [1,2,3,5].

Input: list = 10 -> 20 -> 30 -> 40, n = 4
Output: 20 -> 30 -> 40
Explanation: The 4th node from the end is "10", so after removing it, the list becomes [20,30,40].

Input: list = 7 -> 14 -> 21 -> 28 -> 35, n = 3
Output: 7 -> 14 -> 28 -> 35
Explanation: The 3rd node from the end is "21", so after removing it, the list becomes [7,14,28,35]
'''

# solution one using dummy node ot simplify edge cases handling
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def removeNth(self, head, n):
        # create a dummy node to simplify edge cases since the head might be deleted
        dummy = Node(0)
        dummy.next = head

        # create two pointers, first and second, and set them to the dummy one
        first = dummy
        second = dummy

        # move first pointer n nodes ahead to build the gap
        for _ in range(n + 1):
            first = first.next

        # move first to the end, maintaining the gap
        # so that second points to the node to be deleted
        while first:
            first = first.next
            second = second.next

        # remove the nth node from the end by skipping it
        second.next = second.next.next

        # return the next of the dummy which will be the new head
        return dummy.next

# solution two
# Complexity:
# O(n) time - where n is the length of the input string
# O(1) space
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def removeNth(self, head, n):
        size = 0
        node = head
        while node:
            node = node.next
            size += 1

        # position of the node to remove
        k = size - n

        # move to the node before the one to remove
        # so that prev will be the node before the one to remove
        # and current will be the node to remove
        prev = None
        current = head
        for _ in range(k):
            prev = current
            current = current.next

        # if prev and current are not None, means we found the node to remove
        if prev and current:
            prev.next = current.next
        # prev is None when we want to remove the first node
        elif not prev:
            # if list has more nodes, we move the head to the next one
            if size > 1:
                head = head.next
            # otherwise we set head = None
            # (prev is also None, so we could do head = prev)
            else:
                head = None

        return head
